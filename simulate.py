def E(dfNodes, kM, M, commT, idlePower, coef):
    # VAFSA策略中，搜索固定k_M时的最优节点，k_M从M-1开始
    node = range(kM+1)
    durations = dfNodes.iloc[node]['duration'].values
    maxT = max(durations)
    powers = dfNodes.iloc[node]['power'].values
    indexs = dfNodes.iloc[node].index.values
    powerList = []
    for i in range(kM+1):
        x = durations[i]/maxT
        powerDVFS = (coef['A']*x**3+coef['B']*x**2+coef['C']*x+coef['D'])*powers[i]
        powerList.append(powerDVFS)
    values, best_indices = find_smallest_m_numbers(powerList[:-1], M-1)
    E_min_fixk = (sum(values) + powerList[-1])*maxT + M*idlePower*commT
    perf_fixk = 1000/(maxT+commT)
    best_ID = [indexs[b] for b in best_indices]
    best_ID.append(indexs[-1])
    return E_min_fixk, best_ID, perf_fixk