"""Dimensionality-reduction utilities.
[EXPERIMENTAL] Not integrated into the canonical figure renderer.

This module implements PCA and neighborhood-preservation diagnostics. The
historical ``TSNEProjection`` class remains as an explicit unsupported
compatibility surface; the repository does not ship a fake t-SNE algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

import numpy as np


@dataclass
class ProjectionResult:
    embedding: np.ndarray
    method: str
    parameters: Dict[str, object]
    diagnostics: Dict[str, float]


class PCAProjection:
    """Principal-component projection using a centered SVD."""

    def __init__(self, n_components: int = 2):
        if n_components < 1:
            raise ValueError("n_components must be >= 1")
        self.n_components = n_components
        self.mean_: Optional[np.ndarray] = None
        self.components_: Optional[np.ndarray] = None
        self.explained_variance_: Optional[np.ndarray] = None
        self.explained_variance_ratio_: Optional[np.ndarray] = None

    @staticmethod
    def _validate(X) -> np.ndarray:
        array = np.asarray(X, dtype=float)
        if array.ndim != 2:
            raise ValueError("X must be a 2D array")
        if array.shape[0] < 2:
            raise ValueError("PCA requires at least two observations")
        if array.shape[1] < 1:
            raise ValueError("PCA requires at least one feature")
        if not np.isfinite(array).all():
            raise ValueError("X contains NaN or infinite values")
        return array

    def fit(self, X) -> "PCAProjection":
        array = self._validate(X)
        if self.n_components > min(array.shape):
            raise ValueError(
                f"n_components={self.n_components} exceeds min(X.shape)={min(array.shape)}"
            )
        self.mean_ = array.mean(axis=0)
        centered = array - self.mean_
        _, singular_values, vt = np.linalg.svd(centered, full_matrices=False)
        self.components_ = vt[: self.n_components]
        variance = (singular_values ** 2) / (array.shape[0] - 1)
        self.explained_variance_ = variance[: self.n_components]
        total = variance.sum()
        self.explained_variance_ratio_ = (
            self.explained_variance_ / total if total > 0 else np.zeros_like(self.explained_variance_)
        )
        return self

    def transform(self, X) -> np.ndarray:
        if self.mean_ is None or self.components_ is None:
            raise RuntimeError("PCAProjection must be fitted before transform")
        array = np.asarray(X, dtype=float)
        if array.ndim != 2 or array.shape[1] != self.mean_.shape[0]:
            raise ValueError("X feature dimension does not match fitted PCA")
        if not np.isfinite(array).all():
            raise ValueError("X contains NaN or infinite values")
        return (array - self.mean_) @ self.components_.T

    def fit_transform(self, X) -> np.ndarray:
        return self.fit(X).transform(X)

    def result(self, X) -> ProjectionResult:
        embedding = self.fit_transform(X)
        return ProjectionResult(
            embedding=embedding,
            method="pca",
            parameters={"n_components": self.n_components, "centered": True},
            diagnostics={
                "explained_variance_ratio_sum": float(self.explained_variance_ratio_.sum()),
            },
        )


class TSNEProjection:
    """Compatibility placeholder: a real t-SNE implementation is not shipped."""

    def __init__(self, *args, **kwargs):
        self.parameters = dict(kwargs)
        if args:
            self.parameters["positional_args"] = list(args)

    def fit_transform(self, X):
        raise NotImplementedError(
            "sci-render-kit does not implement t-SNE. Use a validated external implementation "
            "and pass its embedding to the rendering layer with provenance."
        )


class ProjectionMetrics:
    """Neighborhood and distance diagnostics for an externally produced embedding."""

    @staticmethod
    def _validate_pair(original, embedded):
        X = np.asarray(original, dtype=float)
        Y = np.asarray(embedded, dtype=float)
        if X.ndim != 2 or Y.ndim != 2:
            raise ValueError("original and embedded must be 2D arrays")
        if X.shape[0] != Y.shape[0]:
            raise ValueError("original and embedded must contain the same observations")
        if X.shape[0] < 3:
            raise ValueError("at least three observations are required")
        if not np.isfinite(X).all() or not np.isfinite(Y).all():
            raise ValueError("arrays contain NaN or infinite values")
        return X, Y

    @staticmethod
    def _pairwise_distances(X: np.ndarray) -> np.ndarray:
        delta = X[:, None, :] - X[None, :, :]
        return np.sqrt(np.sum(delta * delta, axis=2))

    @staticmethod
    def _rank_matrix(distances: np.ndarray) -> np.ndarray:
        """Return 1-based neighbor ranks; diagonal self-rank is zero."""
        n = distances.shape[0]
        ranks = np.zeros((n, n), dtype=int)
        for i in range(n):
            order = np.argsort(distances[i], kind="stable")
            rank = 1
            for j in order:
                if j == i:
                    continue
                ranks[i, j] = rank
                rank += 1
        return ranks

    @staticmethod
    def _validate_k(n: int, k: int) -> int:
        k = int(k)
        if k < 1:
            raise ValueError("k must be >= 1")
        if k >= n:
            raise ValueError("k must be smaller than number of observations")
        denominator = n * k * (2 * n - 3 * k - 1)
        if denominator <= 0:
            raise ValueError("k is too large for the trustworthiness/continuity normalization")
        return k

    @classmethod
    def trustworthiness(cls, original, embedded, k: int = 5) -> float:
        """Measure false-neighbor intrusion into the embedding (higher is better)."""
        X, Y = cls._validate_pair(original, embedded)
        n = X.shape[0]
        k = cls._validate_k(n, k)
        d_x = cls._pairwise_distances(X)
        d_y = cls._pairwise_distances(Y)
        rank_x = cls._rank_matrix(d_x)
        penalty = 0.0
        for i in range(n):
            neighbors_y = [j for j in np.argsort(d_y[i]) if j != i][:k]
            for j in neighbors_y:
                if rank_x[i, j] > k:
                    penalty += rank_x[i, j] - k
        normalizer = 2.0 / (n * k * (2 * n - 3 * k - 1))
        return float(max(0.0, min(1.0, 1.0 - normalizer * penalty)))

    @classmethod
    def continuity(cls, original, embedded, k: int = 5) -> float:
        """Measure original-neighbor preservation in the embedding (higher is better)."""
        X, Y = cls._validate_pair(original, embedded)
        n = X.shape[0]
        k = cls._validate_k(n, k)
        d_x = cls._pairwise_distances(X)
        d_y = cls._pairwise_distances(Y)
        rank_y = cls._rank_matrix(d_y)
        penalty = 0.0
        for i in range(n):
            neighbors_x = [j for j in np.argsort(d_x[i]) if j != i][:k]
            for j in neighbors_x:
                if rank_y[i, j] > k:
                    penalty += rank_y[i, j] - k
        normalizer = 2.0 / (n * k * (2 * n - 3 * k - 1))
        return float(max(0.0, min(1.0, 1.0 - normalizer * penalty)))

    @classmethod
    def normalized_stress(cls, original, embedded) -> float:
        """Distance distortion after optimal scalar rescaling of embedded distances."""
        X, Y = cls._validate_pair(original, embedded)
        d_x = cls._pairwise_distances(X)
        d_y = cls._pairwise_distances(Y)
        tri = np.triu_indices_from(d_x, k=1)
        original_dist = d_x[tri]
        embedded_dist = d_y[tri]
        denominator = float(np.dot(embedded_dist, embedded_dist))
        scale = float(np.dot(original_dist, embedded_dist) / denominator) if denominator > 0 else 0.0
        residual = original_dist - scale * embedded_dist
        original_energy = float(np.dot(original_dist, original_dist))
        if original_energy == 0:
            return 0.0 if np.allclose(residual, 0) else float("inf")
        return float(np.sqrt(np.dot(residual, residual) / original_energy))


class ProjectionEngine:
    """Small explicit registry for implemented projection methods."""

    def __init__(self):
        self._methods = {"pca": PCAProjection}

    def project(self, X, method: str = "pca", **kwargs) -> ProjectionResult:
        method = str(method).lower()
        if method == "tsne":
            raise NotImplementedError("t-SNE is not implemented; use an external validated embedding")
        if method not in self._methods:
            raise ValueError(f"unknown projection method: {method}")
        projector = self._methods[method](**kwargs)
        return projector.result(X)
