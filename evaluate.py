"""Evaluate saved test-set predictions on Hangzhou (HZMetro) with the metrics used in the paper.

Metrics (computed on predictions rounded to non-negative integers, rint(clip(pred, 0))):
  wMAPE (all)      = sum |y_hat - y| / sum y                      (%)
  wMAPE (nonzero)  = sum over cells with y > 0 of |y_hat - y| / sum y   (%; same denominator)
  MAE, RMSE        = averaged over all N x N OD cells and all test slots

Each prediction file is an .npz with one array "pred" of shape (T, N, N).
The ground truth is an .npz with one array "y" of the same shape.

Usage:
  python evaluate.py --gt hz_test_y.npz --pred predictions/hz/hast_seed*.npz
"""
import argparse
import glob

import numpy as np


def metrics(pred, y):
    q = np.rint(np.clip(pred, 0, None))
    e = np.abs(q - y)
    return np.array([100 * e.sum() / y.sum(), 100 * e[y > 0].sum() / y.sum(), e.mean(), np.sqrt(((q - y) ** 2).mean())])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gt", required=True)
    ap.add_argument("--pred", nargs="+", required=True)
    a = ap.parse_args()
    y = np.load(a.gt)["y"].astype("float64")
    files = sorted(f for x in a.pred for f in (glob.glob(x) or [x]))
    rows = []
    for f in files:
        p = np.load(f)["pred"].astype("float64")
        assert p.shape == y.shape, (f, p.shape, y.shape)
        m = metrics(p, y)
        rows.append(m)
        print(f"{f}: wMAPE {m[0]:.2f}  wMAPE-nz {m[1]:.2f}  MAE {m[2]:.3f}  RMSE {m[3]:.3f}")
    r = np.array(rows)
    mu = r.mean(0)
    sd = r.std(0, ddof=1) if len(r) > 1 else np.zeros(4)
    print(f"mean ({len(r)} runs): wMAPE {mu[0]:.2f} ± {sd[0]:.2f}  wMAPE-nz {mu[1]:.2f} ± {sd[1]:.2f}  MAE {mu[2]:.3f}  RMSE {mu[3]:.3f}")


if __name__ == "__main__":
    main()
