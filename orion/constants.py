"""
orion.constants

Module for storing constants across orion.
"""

EDIVISIVE="EDivisive"
ISOLATION_FOREST="IsolationForest"
JSON="json"
TEXT="text"
JUNIT="junit"
CMR="cmr"

# Window expansion: when a changepoint is in the first 5 points, we re-validate by
# expanding the lookback window. These values are fixed (no CLI options) for consistency.
#
# CHANGEPOINT_BUFFER (5): Number of initial points considered the "buffer". In the Hunter
# paper, a minimum of 5 points prior and 5 after a point are needed to better include
# a point as a changepoint; we chose 5 for this buffer for that reason.
#
# EXPAND_DAYS (10): Days added to the lookback when expanding the window. 10 days
# gives a reasonable chance to pull in more runs for re-validation in order to ensure we have minimum 5 datapoints for re-validation.
#
# EXPAND_POINTS (5): Extra data points to request when expanding. 5 aligns with the
# buffer size and balances getting more context vs. avoiding over-fetching.
#
CHANGEPOINT_BUFFER = 5
EXPAND_DAYS = 10
EXPAND_POINTS = 5
