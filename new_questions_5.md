### Intermediate Scenarios (100 questions)

#### Series 5.1: Convertible Arbitrage & Credit (15 questions)

**5.1.1 - INTERMEDIATE**: Implement convertible arbitrage: buy convertible bond (Par $100, conversion ratio 30, coupon 2%), short 30 shares at stock price $3.33. Design a delta-neutral position. What's your profit if company pays coupon and stock stays flat? What are risks?

**5.1.2 - INTERMEDIATE**: Price a convertible: convert into 40 shares of stock (trading $2.50), so conversion value = $100. Straight bond value (non-convert) = $90 (credit risk). Conversion option embedded value = $100 - $90 = $10. Is this fair?

**5.1.3 - INTERMEDIATE**: A convertible bond's call feature: issuer can redeem at $105 if stock > $4. As investor, how does this affect your upside? Compare your payoff vs owning straight bond and call options separately.

**5.1.4 - INTERMEDIATE**: Convertible arbitrage hedge breaks down: you're long convertible, short stock. Stock drops 20%, credit spread widens 200bps. Convertible bond drops 25% (both equity and credit components). What's your P&L?

**5.1.5 - INTERMEDIATE**: A convertible bond is "forced conversion" (issuer calls bond, forcing conversion). You assumed holding until maturity, but forced conversion changes returns. How do you model forced conversion risk?

**5.1.6 - INTERMEDIATE**: You're holding a position in a corporate bond with CDS. Spread = 150bps. CDS = 120bps. Basis = 30bps (bond wider). Is this arbitrage? What friction prevents you from selling bond, buying CDS?

**5.1.7 - INTERMEDIATE**: A credit fund is net long bonds (100% bonds, 40% short CDS for hedging, net 60% long). If credit spreads widen (bad for bonds, good for CDS shorts), what's net exposure?

**5.1.8 - INTERMEDIATE**: Implement cross-credit arbitrage: bond A (senior) trades 100bps spread, bond B (junior) trades 150bps spread. Normally B trades 50bps wider (for subordination). Basis = 0bps (tight). Opportunity?

**5.1.9 - INTERMEDIATE**: A distressed fund buys a bond at 40 cents on dollar. Expects recovery to 80 cents, generating 100% return. But recovery timeline unknown (1-5 years). What discount rate justifies 40-cent entry? How does time-to-recovery affect IRR?

**5.1.10 - INTERMEDIATE**: You're analyzing a stressed company: EBITDA declining, leverage rising to 5x, bonds trading 300bps over treasuries. What's probability of default? Use Merton model (equity as call option on assets) to calculate.

**5.1.11 - INTERMEDIATE**: A fund's credit portfolio has average spread 150bps, average duration 5 years, leverage 1.5x. If spreads widen 50bps, what's portfolio loss? How does leverage amplify spread widening impact?

**5.1.12 - INTERMEDIATE**: Model a credit manager's performance: 2020 return +15% (spreads tightened from 200bps to 150bps, bonds rallied). 2021 return +8% (carry income + modest price appreciation). 2022 return -20% (spreads widen, rates rise). Are these returns explainable by credit cycle?

**5.1.13 - INTERMEDIATE**: A convertible arbitrage strategy gets hit by negative convexity: stock rises sharply, forced conversion looms, bond declines (conversion limits upside). Then stock falls sharply, bond's embedded put option activates, protecting downside. How do you hedge negative convexity?

**5.1.14 - INTERMEDIATE**: You're analyzing a high-yield bond fund: dividend = 6%, realized credit loss = 1.5% annually (from defaults), net return = 4.5%. Is this justified for high-yield risk? What's your return expectation?

**5.1.15 - INTERMEDIATE**: A fund holds bonds from 10 issuers, correlations normally 0.3. In crisis, correlations spike to 0.8. Default probabilities 2% annually become 10% in crisis. How does this impact portfolio loss distribution? What's 99% VaR in crisis?

#### Series 5.2: Event-Driven & Special Situations (15 questions)

**5.2.1 - INTERMEDIATE**: Model a merger arbitrage: Acquirer bids $50/share for Target (currently $48). Probability deal closes = 80%, timing = 6 months. Risk-free rate = 2%. What's fair value for Target stock? What's arbitrage spread?

**5.2.2 - INTERMEDIATE**: A merger deal has regulatory uncertainty: 50% probability it's blocked. If blocked, stock returns to $40 (from $45 at announcement). If proceeds, stock rises to $50 (deal value). What's risk-adjusted return from entry at $48?

**5.2.3 - INTERMEDIATE**: You're executing merger arb on 10 deals, expected return 3% each (avg deal spread = 1.5%, execution costs = 0.5%). Each deal has 75% success rate. Expected portfolio return after accruals? Standard deviation?

**5.2.4 - INTERMEDIATE**: A special situation: company announces bankruptcy, equity holders expected to get nothing. But bankruptcy trustee discovers hidden assets, leading to equity recovery. Estimate probability of recovery. Build payoff diagram.

**5.2.5 - INTERMEDIATE**: A proxy contest: activist shareholders challenge management. Success probability = 40%, seats won = 3 of 9. If successful, company makes changes, stock rises 20%. If failed, stock slightly declines -5%. Expected return from entry at current price?

**5.2.6 - INTERMEDIATE**: You're analyzing a spinoff: parent company spins off subsidiary. Usually spinoffs outperform initially. Do you buy at announcement or wait for spinoff date? Model market impact, liquidity changes.

**5.2.7 - INTERMEDIATE**: A liquidation event: company liquidating, will return $X to equity holders in 12 months. Calculate NPV for different liquidation values. What's edge if stock trades at 80% of expected value?

**5.2.8 - INTERMEDIATE**: You're analyzing deal certainty: CEO contract has golden parachute if deal blocked. This aligns CEO with deal closure. Is this enough to increase probability? How do you model incentive structure?

**5.2.9 - INTERMEDIATE**: A dividend recapitalization (dividend recap): company borrows $500M, pays special dividend, increases leverage. Equity holders get cash, but company more leveraged. How does this affect equity value? What's the trade-off?

**5.2.10 - INTERMEDIATE**: You're running a special situations fund with 20 positions. 5 are near resolution (4-week to 3-month catalysts), 5 are medium-term (3-12 month catalysts), 10 are long-term (>12 month catalysts). How do you weight expected return vs timing risk?

**5.2.11 - INTERMEDIATE**: Model a going-private transaction: PE fund buys public company for $50/share, takes it private, improves operations, sells for $70/share in 5 years. What's IRR to PE fund? What's return to public shareholders?

**5.2.12 - INTERMEDIATE**: An activist fund buys 5% stake in company (accumulation triggers disclosure). Activist then agitates for changes: board seats, dividend, cost-cutting, strategic review. How long to catalysts? What probability of success?

**5.2.13 - INTERMEDIATE**: You're analyzing a recapitalization: company restructures balance sheet, converts bonds to equity. Dilution to existing shareholders but reduces bankruptcy risk. Is stock likely to rise or fall?

**5.2.14 - INTERMEDIATE**: A fund invests at a "stub value" in a merger: if deal closes, equity worth $50; if blocked, equity worth $35. Probability = 70%. Entry price = $45. What's expected return? What's max loss if deal fails?

**5.2.15 - INTERMEDIATE**: Model deal risk: initially 90% probability, but negative regulatory hearing drops it to 70%, then 50%. Each revision causes stock price adjustment. How do you manage downward probability revisions?

#### Series 5.3: Macro & Thematic Strategies (15 questions)

**5.3.1 - INTERMEDIATE**: A macro fund makes a big call: US yield curve will invert (2-year > 10-year rates), signaling recession. Position: long 2-year bonds, short 10-year bonds. If curve inverts 50bps, what's profit? If curve steepens 50bps, what's loss?

**5.3.2 - INTERMEDIATE**: You're running a geopolitical trade: sanction risk on country X (currency depreciation expected). Buy put options on currency to profit from depreciation. How do you size position given uncertainty? What's max loss (option premium)?

**5.3.3 - INTERMEDIATE**: A thematic fund bets on electric vehicle (EV) adoption: invest in EV companies, battery makers, mining companies for battery metals. Market share: EVs = 2% today, expected 30% in 10 years. Build investment thesis.

**5.3.4 - INTERMEDIATE**: You're making a macro view: China will reopen economy post-zero-COVID, commodity prices will spike. Position: long copper, iron ore, oil. If reopening faster than expected, upside +30%. If slower/postponed, downside -15%. Expected return?

**5.3.5 - INTERMEDIATE**: A bond-focused macro fund bets on country default risk: Argentina is deteriorating (reserves declining, debt unsustainable). Fund shorts bonds, duration short via curve position. How do you quantify default probability? What catalyst?

**5.3.6 - INTERMEDIATE**: You're analyzing a macro strategy's return sources: 40% from currency moves, 30% from equity moves, 20% from commodity moves, 10% from credit spreads. Are these returns from conviction views or just leveraged beta?

**5.3.7 - INTERMEDIATE**: A macro fund's biggest mistake: made correct call on interest rates (rates did fall), but entry timing was off. Entered short bonds 6 months too early, took losses, exited before the big move. How do you teach timely macro entry?

**5.3.8 - INTERMEDIATE**: You're implementing a multi-asset macro strategy: 40% bonds, 30% equities, 20% commodities, 10% currencies. Rebalance quarterly. Does this hedge-like structure generate alpha? Or just track macro factor returns?

**5.3.9 - INTERMEDIATE**: Model a rate hike cycle: Fed raises rates 25bps per meeting, 6 meetings planned. Market prices in initial hikes but becomes uncertain after 3rd hike. Position: short bonds, frontload short duration in early hikes. What's profit path?

**5.3.10 - INTERMEDIATE**: A political event is scheduled (election in 6 months): outcome affects policy (taxes, spending, regulations). Fund makes two scenarios (incumbent re-elected vs opponent wins). Assign probability to each (55% / 45%). Build position reflecting scenario probabilities.

**5.3.11 - INTERMEDIATE**: You're analyzing economic indicators to forecast recession: yield curve inversion, leading indicators declining, unemployment rising. Each indicator has predictive power, but also false positives. How do you weight? When do you make short call?

**5.3.12 - INTERMEDIATE**: A commodity super-cycle thesis: emerging market growth drives commodity demand for 10 years. Fund overweights energy, metals, agriculture. What's the long-term return? What's downside if growth disappoints?

**5.3.13 - INTERMEDIATE**: You're running a sector rotation strategy: Allocate to sectors based on where in economic cycle (early cycle = IT, mid-cycle = industrials, late cycle = utilities, recession = staples). Current cycle phase = mid. Overweight industrials. How does this perform vs static allocation?

**5.3.14 - INTERMEDIATE**: A fund makes bearish calls on tech: overvaluation, rising rates hurt growth stocks, AI hype will disappoint. Position: short tech indices, long utilities. If tech sells off 20%, fund profits. But if market continues higher, losses mount. How to manage convexity?

**5.3.15 - INTERMEDIATE**: Model a long-volatility macro strategy: position in out-of-the-money options (cheap upside/downside protection). Normal times = -2% bleed (theta decay). But in crisis (1-2x/year), portfolio rises 20%. Is tail risk worth theta bleed?

#### Series 5.4: Risk Management & Returns Analysis (15 questions)

**5.4.1 - INTERMEDIATE**: A hedge fund's Sortino ratio (uses downside volatility instead of total volatility) is 1.2, but Sharpe ratio is 0.9. What does this tell you? Is manager taking intelligent risk (downside focus) or just volatility-dampening?

**5.4.2 - INTERMEDIATE**: Analyze fund returns: 2019: +18%, 2020: +8%, 2021: +12%, 2022: -8%. Cumulative return over 4 years = +35% (compound ~8% annual). Is this alpha or beta? How do you decompose?

**5.4.3 - INTERMEDIATE**: A fund's monthly returns: average return = +1%, std dev = 2%. Using historical data, 99% VaR (one month) = -5%. During crisis month in 2008, fund lost -18%. Why did VaR fail? What's the lesson?

**5.4.4 - INTERMEDIATE**: Compare two funds: Fund A (Sharpe 1.5, max drawdown 20%), Fund B (Sharpe 0.8, max drawdown 10%). Which is better? If LPs are risk-averse, which appeals? If they want returns, which appeals?

**5.4.5 - INTERMEDIATE**: A fund has leverage: 2x on long, 1.5x on short (net 0.5x long). If market rises 10%, fund return = 5% (0.5x * 10%). Is this leverage working as intended? What's risk?

**5.4.6 - INTERMEDIATE**: Analyze a fund's performance attribution: Total return = +10%. Explain as: +12% from skill (alpha) - 2% from market timing mistakes. Is alpha real or noise? What's the confidence interval?

**5.4.7 - INTERMEDIATE**: A fund underperforms benchmark in bull markets but outperforms in bear markets. Sharpe ratio is 1.2 vs benchmark 0.9. Is this skill or just low beta? How do you measure alpha correctly?

**5.4.8 - INTERMEDIATE**: Calculate Information Ratio: fund return = 12%, benchmark return = 10%, tracking error = 4%. IR = (12% - 10%) / 4% = 0.5. Is this good? What IR do you expect from skilled managers?

**5.4.9 - INTERMEDIATE**: A fund's returns: monthly returns from +5% to -5%, with negative skew (rare large losses vs frequent small gains). Sharpe ratio based on normal distribution = 1.0. But accounting for skew, true Sharpe = 0.8. Should you reject the fund?

**5.4.10 - INTERMEDIATE**: Analyze persistence: a manager's top quartile 5-year return = +15%. Next 5 years, manager is bottom quartile = +3%. Is this luck or skill decay? How much persistence remains?

**5.4.11 - INTERMEDIATE**: A fund's fees: 2% management fee, 20% performance fee with high-water mark (HWM). Fund starts at $100M, rises to $120M (+20% return), manager gets 20% * $20M = $4M performance fee. Fair?

**5.4.12 - INTERMEDIATE**: A fund's risk management framework: individual position limit 5% of portfolio, sector limit 20%, leverage cap 3x, VaR limit 2% daily. One trader violates position limit (6%), justifying as temporary. How do you handle?

**5.4.13 - INTERMEDIATE**: Model a fund's capital growth: Start $100M, annual management fee 2% = $2M cost, annual return on capital 10% = $10M gain, net growth = $8M. After 5 years, AUM = $140M (with no new subscriptions). What's true growth rate net of fees?

**5.4.14 - INTERMEDIATE**: A fund has redemption pressure: LPs request $50M out of $200M (25% redemption). Fund can meet in cash, but cash = $20M. Must liquidate $30M positions (haircut 5%). What's total impact on remaining LPs' NAV?

**5.4.15 - INTERMEDIATE**: Analyze a fund's risk-adjusted returns using Calmar ratio (return / max drawdown). Return = 15%, max drawdown = 30%. Calmar = 0.5. Compare to benchmark Calmar = 0.3. Does higher Calmar justify investment?

### Advanced Scenarios (75 questions)

#### Series 6.1: Complex Arbitrage & Relative Value (20 questions)

**6.1.1 - ADVANCED**: Implement basis trade: Treasury futures priced at 110.5, spot bond price 110.2. Carry cost = 2bps/month, basis tightens gradually. Hold for 3 months, basis tightens to 1bp. Expected profit = 1bp - 2bp * 3 = -5bp. Is this profitable? When does basis arbitrage fail?

**6.1.2 - ADVANCED**: You're running a multi-asset arbitrage: identify 3 correlated assets (A, B, C) with mispricing. Build a triplet arbitrage (long A, short B, short C in optimized weights). Model cointegration, convergence timeline, hedging ratios.

**6.1.3 - ADVANCED**: Implement capital structure arbitrage: company has bond trading 100, CDS 80, equity trading 200. Use Merton model to decompose equity value into "risk-free" (bonds) + volatility option (equity). Identify mispricings across capital structure.

**6.1.4 - ADVANCED**: You're operating a sovereign arbitrage: two countries (A and B) are economically similar but bond spreads diverge (A spreads 50bps, B spreads 100bps). Position: long A bonds, short B bonds (ratio-hedged). Model mean reversion, risks of status divergence.

**6.1.5 - ADVANCED**: Implement a volatility swap arbitrage: long volatility swap, short realized volatility (short straddle). If realized vol < strike on variance swap, profit. But realize vol can spike unexpectedly (tail risk). How do you manage gamma/tail risk?

**6.1.6 - ADVANCED**: You're running a steepener/flattener trade: on yield curve, short 2-year / long 10-year (curve steepener). If economic growth accelerates, front-end rates rise faster (curve flattens), you lose. How do you hedge? What's a bearish steepener vs bullish?

**6.1.7 - ADVANCED**: Implement a cross-currency basis trade: USD interest rates are 5%, EUR rates are 2.5%. Using covered interest parity, your basis should be zero. But if basis is 50bps (USD forward rates are irrational), arbitrage exists. Model transaction costs, funding costs.

**6.1.8 - ADVANCED**: You're implementing index replication arbitrage: large index fund is rebalancing (buying 100 stocks, selling 100), creating temporary imbalance. You front-run addition (buy before price spike), profit as index fund buys. Scale analysis: how much can you capture?

**6.1.9 - ADVANCED**: Construct a statistical factor-neutral portfolio using PCA: use first 5 principal components to represent market dynamics. Construct factor-neutral portfolio (zero exposure to PCs) to capture non-market alpha. How many positions needed?

**6.1.10 - ADVANCED**: You're using a cointegration approach: identify N-tuple of stocks (typically 10-20) that move together long-term. When tuple diverges (one stock lags), bet on reversion. Model the reversion rate, half-life, stop losses.

**6.1.11 - ADVANCED**: Implement earnings quality arbitrage: company has high reported earnings but low cash flow (revenue quality issue). Short the stock, expecting restatement / markdown. Model probability, timeline, catalyst.

**6.1.12 - ADVANCED**: You're operating a complex relative value strategy: Long high-conviction mispricing in illiquid small-cap (+200bp alpha), short systematic risk factors with liquid instruments (index -0.1% daily cost). Net alpha after costs = 5bp/day. Scalable?

**6.1.13 - ADVANCED**: Model credit-equity relative value: equity price implies 5% default probability, CDS market implies 8% default probability. Mispricing exists. Should you short equity or long CDS? Which captures mispricing more efficiently?

**6.1.14 - ADVANCED**: Implement a multi-leg hedging strategy: long a complex structured product (exotic option), hedge with 15 vanilla instruments. Calculate optimal hedge ratios minimizing residual portfolio variance. Does hedge fully remove tail risk?

**6.1.15 - ADVANCED**: You're managing basis risk in a complex hedge: gold forward contracts have basis relative to spot + futures basis. Multiple basis sources create residual risk. Model combined basis distribution, correlation breakdowns.

**6.1.16 - ADVANCED**: Implement a dynamic arbitrage strategy: prices converge stochastically (mean reversion with random half-life). Should you enter immediately or wait for wider spread? Model optimal entry timing.

**6.1.17 - ADVANCED**: You're running a meta-arbitrage: arbitrage opportunity itself can be traded (on derivatives market). E.g., variance swap market prices divergence from volatility swap market. Construct profitable arbitrage on arbitrage.

**6.1.18 - ADVANCED**: Implement a capital-efficient arbitrage: use derivatives, not outright positions, to capture mispricings. E.g., short calls on overpriced stock, long puts on underpriced stock, minimize notional capital required. How efficient can you make?

**6.1.19 - ADVANCED**: Model basis trades in crisis: normally profitable, basis arbitrage (short volatility, long realized) can face catastrophic losses when correlation structures break. How do you stress-test? What's tail VaR?

**6.1.20 - ADVANCED**: You're implementing a regime-aware arbitrage: arbitrage works only in specific regimes (normal market conditions). In crises (other regime), arbitrage breaks down, losses are large. Build Markov-switching model to detect regime changes dynamically.

#### Series 6.2: Crowded Trades & Systemic Risk (15 questions)

**6.2.1 - ADVANCED**: Analyze crowded trade risk: a popular hedge fund strategy is now implemented by 100+ funds, total $10B allocated. When does crowding become systemic? If 20% of funds need to exit (redemptions), what's market impact?

**6.2.2 - ADVANCED**: Model trade unwind dynamics: a crowded trade unwinds. Funds try to exit together. Initial exits cause losses, triggering stop losses, cascading unwind. Model unwind speed, magnitude, recovery. What's drawdown before reversion?

**6.2.3 - ADVANCED**: You're detecting crowded trades using data: if 50+ fund 13-F filings have similar positions (similar holdings, similar weights), this is crowded. When does crowding matter? How do you profit from crowding (or avoid it)?

**6.2.4 - ADVANCED**: Implement a "crowding-aware" portfolio: reweight positions to reduce exposure to crowded trades. Sacrifice some alpha to reduce crowding tail risk. What's the trade-off? How much alpha loss justifies crowding reduction?

**6.2.5 - ADVANCED**: Model a crowded short: many hedge funds are short the same stock (high short interest). If positive catalyst occurs (earnings beat), short squeeze cascades, stock rises 50%+. Model squeeze magnitude based on short interest, float, funding.

**6.2.6 - ADVANCED**: You're analyzing risk leverage in crowded trades: if all crowded trade participants are on 2x leverage, and 10% drawdown occurs, margin calls cascade, forced deleveraging amplifies drawdown. Model cascade dynamics.

**6.2.7 - ADVANCED**: Detect macro crowding: multiple macro funds are betting on same outcome (e.g., USD strength). If outcome reverses, all exit simultaneously, currency moves against them sharply. What's the unwind dynamic?

**6.2.8 - ADVANCED**: Model information cascade risk: early traders' positions reveal information, herding occurs, position becomes crowded, tail risk emerges. How does cascade differ from fundamental value change? How long does cascade last?

**6.2.9 - ADVANCED**: You're managing crowding in credit: if many credit funds buy same corporate bonds (flight-to-quality), bonds are crowded. Exit crowding early? Wait for price reversion? Model trade-offs.

**6.2.10 - ADVANCED**: Implement a "crowding hedge": if your main strategy is crowded, short a barometer of that crowding (e.g., short most-crowded stock in basket). When crowding unwinds, barometer falls, hedge offsets losses.

**6.2.11 - ADVANCED**: Model regulatory changes' interaction with crowding: if leverage restrictions force 20% position reductions, funds unwind crowded positions first. Model who exits first, cascade magnitude, recovery.

**6.2.12 - ADVANCED**: You're analyzing volatility crowding: VIX-linked products became popular (2x VIX ETN), attracting retail. Crowding in VIX products caused extreme convexity (VIX options expensive). When did this bubble burst? What's cascade risk?

**6.2.13 - ADVANCED**: Detect crowding in factor strategies: value factor is very crowded (many funds own same value positions). Factor reversal risk: if growth outperforms, all factor funds exit together. Model cascade, magnitude.

**6.2.14 - ADVANCED**: You're running a multi-strategy fund with crowding exposure: Strategy A = +$100M alpha but crowded (50 funds), Strategy B = +$30M alpha, uncrowded (5 funds). Allocate capital between crowding/reward trade-off.

**6.2.15 - ADVANCED**: Model systemic implications of crowded trade unwind: if $50B in crowded trade must exit, and market depth is only $5B/day, what's market impact? How do regulators respond? What's circuit-breaker activation risk?

#### Series 6.3: Fund of Funds & Diversification (15 questions)

**6.3.1 - ADVANCED**: Build a fund-of-hedge-funds (FoHF) portfolio: select 20 hedge funds, optimize for maximum risk-adjusted return subject to concentration limits, correlation limits, strategy diversification. How does FoHF Sharpe compare to equal-weighted fund index?

**6.3.2 - ADVANCED**: Model fund selection skill: 50% of hedge funds underperform by 100bps annually vs peers. 50% of top 25% funds outperform next 25% in future period (persistence test). How much selection skill is needed to beat passive indexing?

**6.3.3 - ADVANCED**: Analyze FoHF fee structure: FoHF charges 1% + 10% on top of underlying funds' 2% + 20%. Total fee = ~3.2% + 28% (compounded). True net fee is 10% of original capital. How much alpha must FoHF generate to justify?

**6.3.4 - ADVANCED**: Model diversification across fund strategies: design portfolio with Long/Short Equity (15%), Credit Arbitrage (25%), Multi-Strategy (20%), Macro (15%), Event-Driven (15%), Quant (10%). Expected return 9%, volatility 8%. What's beta to equities? Is this low enough?

**6.3.5 - ADVANCED**: Implement conditional allocation model: allocate more capital to strategies when they're out-of-favor (expected return higher). Allocate less when crowded (valuation high). Does this dynamic allocation add alpha?

**6.3.6 - ADVANCED**: Model tail dependence in FoHF portfolio: funds have correlation 0.3 normally, spike to 0.8 in crises. Build portfolio with correlation stress-tested. What's drawdown under correlation breakdown scenario?

**6.3.7 - ADVANCED**: Analyze vintage year effects: hedge funds started in 1998 (pre-crisis) underperform those started in 2009 (post-crisis), driven by selection bias (bad 1998 funds closed, winners survived). How do you account for survivorship bias?

**6.3.8 - ADVANCED**: Model redemption dynamics in FoHF: if LPs redeem 30% from FoHF, FoHF must redeem from underlying funds. Many underlying funds may gate redemptions. What's liquidity cascade risk? How much liquidity buffer needed?

**6.3.9 - ADVANCED**: Implement a value-tilted FoHF strategy: identify undervalued hedge funds (low valuations on NAV, discount to intrinsic worth). Long undvalued, short overvalued. Does this value tilt within FoHF generate alpha?

**6.3.10 - ADVANCED**: Model counterparty concentration in FoHF: all underlying funds use same prime brokers (Tier 1 only). If a prime broker fails, funds face operational risk (positions frozen). How do you diversify this risk?

**6.3.11 - ADVANCED**: Analyze style drift in FoHF: underlying funds are classified as "Long/Short Equity" but over time, drift into macro (style drift). This changes portfolio risk profile unintentionally. How do you monitor for drift?

**6.3.12 - ADVANCED**: Model capacity constraints in FoHF: some hedge funds have high capacity (can accept $500M new), others low (can accept $50M only). How does capacity affect FoHF sizing? Do small funds outperform due to better positioning?

**6.3.13 - ADVANCED**: Implement systematic rebalancing in FoHF: monthly rebalancing vs quarterly vs annual. Each rebalancing costs 0.3% (trading costs, market impact). Does more frequent rebalancing improve risk-adjusted returns? Optimal frequency?

**6.3.14 - ADVANCED**: Model FoHF performance during crises: in 2008, average hedge fund down 18%, but FoHF (diversified) down 12% (benefit of diversification). Is diversification enough to justify FoHF structure? Or should LPs go direct to hedge funds?

**6.3.15 - ADVANCED**: Implement an ESG-tilted FoHF: screen out 30% of hedge fund universe (those with poor ESG practices). Does ESG constraint hurt performance? Does ESG diversification add risk?

#### Series 6.4: Performance Analysis & Manager Selection (15 questions)

**6.4.1 - ADVANCED**: Use Bayesian analysis to infer true manager skill from observed returns. Assume prior distribution on manager skill (normal distribution, μ = 0% alpha, σ = 2%). Observe 5 years data: return +12%, benchmark +8%, tracking error 4%. What's posterior on manager skill?

**6.4.2 - ADVANCED**: Analyze performance persistence: split managers into top/bottom quartile based on 5-year returns. How much persistence in next 5 years? Is persistence sufficient for outperformance vs transaction costs in manager selection?

**6.4.3 - ADVANCED**: Implement Monte Carlo analysis: draw 1,000 random return streams matching observed statistics (mean, std dev, skew, kurtosis) of candidate manager. How many of 1,000 paths exceed management fee breakeven? What's the probability that manager underperforms by >2%?

**6.4.4 - ADVANCED**: Use factor analysis to decompose manager returns: manager return = α + β₁*Market + β₂*Size + β₃*Value + β₄*Momentum + ε. What percentage of return is alpha vs beta factors? Do beta factors explain most return?

**6.4.5 - ADVANCED**: Implement multi-factor model selection: compare 3, 5, and 7-factor models on explanatory power (R²). How many factors are needed? Does adding factors overfit (worse out-of-sample)?

**6.4.6 - ADVANCED**: Calculate rolling alpha: compute manager's alpha over 12-month rolling windows. How stable is alpha? Does it decay over time? Are high-alpha years followed by low-alpha years (mean reversion of alpha)?

**6.4.7 - ADVANCED**: Analyze skill vs luck using time-series simulations: simulate 1,000 managers, each with 40% true alpha (0.4% annual), rest is random. How many of 1,000 would show >1% alpha by chance? Does observed alpha represent skill or luck?

**6.4.8 - ADVANCED**: Model manager capacity: smaller funds (< $500M AUM) have alpha 2%, medium (< $5B AUM) have alpha 1%, large (> $5B) have alpha 0.5%. As fund grows, alpha declines due to capacity constraints. Where is the sweet spot?

**6.4.9 - ADVANCED**: Implement meta-analysis of manager performance: combine 100 hedge fund studies, each testing manager alpha. Use meta-regression to estimate true effect size. What's the average true alpha? How much heterogeneity across studies?

**6.4.10 - ADVANCED**: Analyze survivorship bias: compute average returns of all funds (including dead funds = -60% at death) vs survivors only (average return +10%). True population return = weighted average between survivors and dead. How much does survivorship inflate alpha?

**6.4.11 - ADVANCED**: Model luck distribution in returns: if manager has 0% true alpha, what's the distribution of observed returns? For 10-year period, what's the probability of observing +8% annual return by pure chance? Is observed 8% return significant?

**6.4.12 - ADVANCED**: Implement stress-test on manager claims: manager says "never down >10% in any year." Test: what's actual maximum drawdown over 3-month periods? Some 3-month periods likely >10%. Does manager's claim hold under scrutiny?

**6.4.13 - ADVANCED**: Use Bayesian model averaging: don't pick one model of manager skill, but average across multiple models (normal distribution, t-distribution, mixture models). Does model averaging improve forecast accuracy of future returns?

**6.4.14 - ADVANCED**: Analyze skill decay: manager's first 5 years: 2% alpha, next 5 years: 1.5% alpha, last 5 years: 0.8% alpha. Is this skill decay, or investor selection (best investors leave)? How do you distinguish?

**6.4.15 - ADVANCED**: Model manager reputation: famous manager's fund charges 3% + 25%, unknown manager charges 1% + 15%. Both have same true alpha (1%). Which is better for LPs? How much do you pay for brand?

#### Series 6.5: Market Crashes & Recovery Dynamics (10 questions)

**6.5.1 - ADVANCED**: Model a market crash: equity down 20% day 1, down 10% day 2 (cascade, continued selling). Day 3: stabilize (no further falls, slight recovery). Compare this to smooth 20% drop over 3 days. Which path causes more hedge fund damage? Why?

**6.5.2 - ADVANCED**: During the 2020 COVID crash: VIX spiked 400%, equity vol tripled, credit spreads jumped 400bps. Correlations spiked to 0.95. Liquidity dried up. Estimate portfolio loss for: 60% stocks / 40% bonds (should be stable, but isn't). What's true drawdown?

**6.5.3 - ADVANCED**: Model a deleveraging spiral: hedge funds are 1.5x levered on average. Market down 15%, equity losses = 22.5%, AUM decline triggers automatic deleveraging. Each fund reduces 10%. Forced selling depresses market further (15% → 18%), cascading.

**6.5.4 - ADVANCED**: Analyze prime broker risk during crashes: when volatility spikes, prime brokers increase haircuts 100-200%, margin calls spike, funds forced to liquidate. Estimate time to unwind $100B hedge fund positions if market depth only $5B/day.

**6.5.5 - ADVANCED**: Model liquidity drying up: during crash, bid-ask spreads widen 20x. $1B equity position that normally trades $50M/day now trades $5M/day. Time to liquidate = 200 days. If fund needs to liquidate in 10 days, must sell at 50% discount.

**6.5.6 - ADVANCED**: During recovery phase: market falls 30% in crash, then recovers 25% from lows (net still -7.5%). Hedge funds that "bought the dip" (added long positions at bottoms) outperformed. Model recovery dynamics, rebound magnitudes across recoveries.

**6.5.7 - ADVANCED**: Analyze post-crash correlations: after 2008 crash, correlations remained elevated for 6+ months, then normalized. During recovery, what's the typical correlation persistence? How does this affect diversification in recovery phase?

**6.5.8 - ADVANCED**: Model sector rotation during recovery: Energy, Utilities, Staples held up (low volatility in crash), but Tech/Growth crashed hard. In recovery, Tech leads upside (highest volatility in recovery). Model relative outperformance in recovery vs crash.

**6.5.9 - ADVANCED**: Analyze behavioral responses during crashes: retail traders panic-sell, professionals buy dips. Model the flow imbalance: if retail forced selling is $10B and pro buying is $5B, net selling = $5B, prices tank further before stabilizing.

**6.5.10 - ADVANCED**: Model option-driven crashes: portfolio insurance (automatic selling if markets fall) was blamed for 1987 crash severity. If $50B in portfolio insurance activates during 10% down day, what's market impact? Does this cascad into worse outcomes?
