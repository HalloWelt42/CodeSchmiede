def muenz_wechsel(muenzen: list[int], betrag: int) -> int:
    if betrag == 0:
        return 0
    INF = float("inf")
    dp = [INF] * (betrag + 1)
    dp[0] = 0
    for k in range(1, betrag + 1):
        for m in muenzen:
            if m <= k and dp[k - m] + 1 < dp[k]:
                dp[k] = dp[k - m] + 1
    return int(dp[betrag]) if dp[betrag] != INF else -1
