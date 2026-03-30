import os

nav_html = """
    <nav class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all">
        <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="index.html" class="font-bold text-slate-900 tracking-tight flex items-center gap-2">
                <div class="w-6 h-6 bg-blue-600 rounded-md"></div>
                Trade<span class="text-blue-600">Sim</span>
            </a>
            <div class="hidden lg:flex space-x-6 text-sm font-medium text-slate-600">
                <a href="index.html" class="hover:text-blue-600 transition-colors">1. The Problem</a>
                <a href="data.html" class="hover:text-blue-600 transition-colors">2. Data Pipeline</a>
                <a href="ai_models.html" class="hover:text-blue-600 transition-colors">3. AI & Forecasting</a>
                <a href="policy_engine.html" class="hover:text-blue-600 transition-colors">4. Policy Engine</a>
            </div>
            <!-- Mobile Menu Button could go here -->
        </div>
    </nav>
"""

head_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; }}
        .bg-grid {{ background-size: 24px 24px; background-image: linear-gradient(to right, rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.05) 1px, transparent 1px); }}
        .zoom-img {{ transition: transform 0.3s ease; }}
        .zoom-img:hover {{ transform: scale(1.02); }}
    </style>
</head>
<body class="text-slate-800 antialiased pt-16">
{nav}
"""

footer_html = """
    <footer class="border-t border-slate-200 bg-white py-12 text-center mt-16">
        <div class="max-w-6xl mx-auto px-6">
            <div class="text-blue-600 font-bold text-xl mb-4 tracking-tight">TradeSim</div>
            <p class="text-slate-500 text-sm font-medium leading-relaxed max-w-xl mx-auto">
                AI-Enabled Policy Simulation System &copy; 2026<br>
                <span class="text-slate-400 font-normal mt-1 inline-block">Developed by Sajal Garg (IIT2023035)</span>
            </p>
        </div>
    </footer>
</body>
</html>
"""

# PAGE 1: INDEX
index_content = head_html.format(title="The Problem | AI Policy Simulation", nav=nav_html) + """
    <header class="relative bg-slate-950 text-white py-24 overflow-hidden">
        <div class="absolute inset-0 bg-grid z-0"></div>
        <div class="max-w-4xl mx-auto px-6 relative z-10 text-center">
            <h1 class="text-4xl md:text-6xl font-extrabold mb-6 text-slate-50">Understanding the <span class="text-blue-400">Global Shock</span></h1>
            <p class="text-xl text-slate-400 leading-relaxed mb-8">What happens to an emerging economy like India when the world's two biggest markets join forces without them?</p>
            <div class="flex justify-center gap-4">
                <a href="data.html" class="bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 px-6 rounded-lg transition-colors">See the Data Framework &rarr;</a>
            </div>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-16 space-y-16">
        <section class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
            <h2 class="text-3xl font-bold mb-6">The Real-World Problem Explained</h2>
            <div class="prose prose-slate max-w-none space-y-6 text-lg text-slate-600">
                <p>Imagine the global economy as a massive highway system. Every country is a major city, and <strong>Free Trade Agreements (FTAs)</strong> are high-speed expressways built between them. Goods travel down these expressways fast and cheap, because there are zero toll booths (tariffs).</p>
                <p>Now, what happens if the <strong>European Union (EU)</strong> and the <strong>United States (USA)</strong>—two of the richest "cities" in the world—build an exclusive, ultra-fast expressway just for themselves? They start trading heavily with each other because it's cheaper. But what about countries not on that expressway?</p>
                <div class="bg-blue-50 p-6 rounded-xl border-l-4 border-blue-500 text-blue-900">
                    <h3 class="font-bold mb-2">Trade Diversion: The Silent Killer</h3>
                    <p class="text-base">This is called <strong>Trade Diversion</strong>. The EU and USA aren't attacking India, but by making it incredibly cheap to trade with each other, India's exports suddenly look more expensive. Buyers in the US who used to buy Indian textiles or electronics might now buy them from Europe because there are no longer any tariffs.</p>
                </div>
                <p>For India, this means <strong>lost jobs, closed factories, and broken supply chains</strong> in critical sectors like auto parts, pharmaceuticals, and machinery. It means being pushed out of the "Global Value Chain"—the international assembly line where products are made.</p>
            </div>
        </section>

        <section class="space-y-8">
            <h2 class="text-3xl font-bold text-center">Our Research Objectives</h2>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white p-6 rounded-xl shadow-sm border-t-4 border-red-500">
                    <h3 class="font-bold text-lg mb-2">1. Measure the Damage</h3>
                    <p class="text-slate-600">Exactly how much money and trade volume will India lose? Which industries will be hit the hardest by this new EU-US trade express lane?</p>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border-t-4 border-amber-500">
                    <h3 class="font-bold text-lg mb-2">2. Test the Cures</h3>
                    <p class="text-slate-600">If the government has a limited budget, should they hand out cash subsidies to factories, or spend years negotiating new treaties with other countries?</p>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-sm border-t-4 border-emerald-500">
                    <h3 class="font-bold text-lg mb-2">3. Automate Policy</h3>
                    <p class="text-slate-600">Can an AI safely guide a government through a 10-year economic war, maximizing survival while keeping the budget balanced?</p>
                </div>
            </div>
        </section>

        <section class="bg-slate-900 text-white p-8 rounded-2xl">
            <h2 class="text-2xl font-bold mb-4">How we solved this (The System Pipeline)</h2>
            <p class="text-slate-300 mb-6">To answer these questions, we couldn't just guess. We built a digital twin of international trade using 8 advanced AI steps:</p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center text-sm">
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>1. Data</strong><br><span class="text-slate-400">Merge databases</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>2. Networks</strong><br><span class="text-slate-400">Map global routes</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>3. Shock</strong><br><span class="text-slate-400">Simulate the FTA</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>4. Predict (ML)</strong><br><span class="text-slate-400">XGBoost & LSTM</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>5. Explain (XAI)</strong><br><span class="text-slate-400">SHAP feature drivers</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>6. Valid (GNN)</strong><br><span class="text-slate-400">Graph geometry changes</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700"><strong>7. Test (Causal)</strong><br><span class="text-slate-400">Causal Forests ATE</span></div>
                <div class="bg-slate-800 p-4 rounded-lg border border-slate-700 text-emerald-400 border-emerald-800"><strong>8. Optimize (RL)</strong><br><span>AI Decision Engine</span></div>
            </div>
        </section>

        <div class="text-center pt-8">
            <a href="data.html" class="inline-block bg-slate-900 text-white font-bold py-4 px-8 rounded-xl hover:bg-slate-800 transition">Next: See How We Built The Data Engine &rarr;</a>
        </div>
    </main>
""" + footer_html

# PAGE 2: DATA
data_content = head_html.format(title="Data Pipeline | AI Policy Simulation", nav=nav_html) + """
    <header class="bg-blue-600 text-white py-16">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h1 class="text-4xl font-extrabold mb-4">Building a Digital Twin of Global Trade</h1>
            <p class="text-xl text-blue-100">Step 1: Gathering the raw materials to train the AI.</p>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-16 space-y-16">
        <section>
            <h2 class="text-3xl font-bold mb-6">Where does the information come from?</h2>
            <p class="text-lg text-slate-600 mb-8">Before an AI can predict economic crashes, it needs to learn the rules of the world. We combined five massive, distinct, real-world databases spanning 20 years. Think of it like teaching the AI history, geography, and math all at once.</p>
            
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-white p-6 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-xl text-slate-800 mb-2">1. WTO / WITS</h3>
                    <p class="text-sm text-slate-600"><strong>The Tax Code:</strong> Tracks exact tariff rates across borders. This tells our model exactly how expensive it is to send goods from one country to another.</p>
                </div>
                <div class="bg-white p-6 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-xl text-slate-800 mb-2">2. UN Comtrade</h3>
                    <p class="text-sm text-slate-600"><strong>The Ledger:</strong> The actual dollar amounts of what countries buy and sell. The raw measurement of export volume.</p>
                </div>
                <div class="bg-white p-6 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-xl text-slate-800 mb-2">3. OECD ICIO</h3>
                    <p class="text-sm text-slate-600"><strong>The Supply Chain:</strong> Measures "Value Added". E.g., if a car is assembled in Germany but uses Indian steel, this database tracks where the real money went.</p>
                </div>
                <div class="bg-white p-6 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-xl text-slate-800 mb-2">4. Supply Graph nodes</h3>
                    <p class="text-sm text-slate-600"><strong>The Network:</strong> Converts trade routes into mathematical "nodes" and "edges" (like dots connected by strings) to see the web of the world.</p>
                </div>
            </div>
        </section>

        <section class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
            <h2 class="text-2xl font-bold mb-4">Making Sense of It All (Feature Engineering)</h2>
            <p class="text-slate-600 mb-6">The AI doesn't just read dollar amounts. We engineered specific "smart features" to help the AI understand the country's posture and strength:</p>
            
            <ul class="space-y-4">
                <li class="flex items-start">
                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold mr-4">1</div>
                    <div>
                        <strong class="block text-slate-900">Out-Degree Centrality</strong>
                        <span class="text-slate-600 text-sm">How many direct trading partners does an industry have? E.g., If India's auto sector only sells to the USA, its centrality is low (fragile). If it sells to 50 countries, it's high (secure).</span>
                    </div>
                </li>
                <li class="flex items-start">
                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold mr-4">2</div>
                    <div>
                        <strong class="block text-slate-900">Dependency Ratio</strong>
                        <span class="text-slate-600 text-sm">Does this industry build things from scratch, or does it rely heavily on imported raw materials to function?</span>
                    </div>
                </li>
                <li class="flex items-start">
                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold mr-4">3</div>
                    <div>
                        <strong class="block text-slate-900">Tariff Differentials</strong>
                        <span class="text-slate-600 text-sm">The delta between what India pays to export to the US vs what the EU pays.</span>
                    </div>
                </li>
            </ul>
        </section>

        <div class="text-center pt-8">
            <a href="ai_models.html" class="inline-block bg-slate-900 text-white font-bold py-4 px-8 rounded-xl hover:bg-slate-800 transition">Next: Applying the AI & Models &rarr;</a>
        </div>
    </main>
""" + footer_html

# PAGE 3: AI MODELS
ai_content = head_html.format(title="AI & Forecasting | AI Policy Simulation", nav=nav_html) + """
    <header class="bg-indigo-900 text-white py-16">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h1 class="text-4xl font-extrabold mb-4">Forecasting & Explainable AI</h1>
            <p class="text-xl text-indigo-200">How the models predict the economic damage—and explicitly explain why.</p>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-16 space-y-20">
        
        <!-- LSTM -->
        <section>
            <div class="bg-indigo-50 text-indigo-800 text-sm font-bold uppercase tracking-widest px-3 py-1 rounded inline-block mb-4">Phase 1: Time Travel</div>
            <h2 class="text-3xl font-bold mb-4">1. LSTM: Predicting the Trajectory of the Crash</h2>
            <p class="text-lg text-slate-600 mb-6">First, we need to know what the future looks like immediately after the EU and USA sign their exclusive treaty. We use a neural network called <strong>LSTM (Long Short-Term Memory)</strong>—an algorithm specifically designed to understand momentum and time.</p>
            
            <figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm mb-6">
                <img src="./images/07_lstm_forecast.png" alt="LSTM Forecast" class="w-full h-auto rounded-lg zoom-img" loading="lazy">
                <figcaption class="mt-4 text-sm text-slate-500 bg-slate-50 p-4 rounded-lg">
                    <strong class="text-slate-900">What you are looking at:</strong> The blue line is historical, normal trade. The red line represents the AI's forecast of trade volume after the shock.<br><br>
                    <strong class="text-teal-700">The Takeaway:</strong> Trade doesn't quickly bounce back. Once those global trade routes are disrupted by the "expressway," the volume steadily decays over years. 
                </figcaption>
            </figure>
        </section>

        <hr class="border-slate-200">

        <!-- XGBOOST & SHAP -->
        <section>
            <div class="flex flex-col md:flex-row gap-12">
                <div class="flex-1">
                    <div class="bg-orange-50 text-orange-800 text-sm font-bold uppercase tracking-widest px-3 py-1 rounded inline-block mb-4">Phase 2: Volume Loss & The "Why"</div>
                    <h2 class="text-3xl font-bold mb-4">2. XGBoost + SHAP</h2>
                    <p class="text-slate-600 mb-4">If LSTM gives us the timeline, <strong>XGBoost</strong> gives us the exact financial numbers. It's a massive decision-tree algorithm that calculated precisely how badly each sector is damaged.</p>
                    <p class="text-slate-600 mb-4">But AI is often a "black box" (it gives an answer, but won't tell you how it got there). Policy makers can't gamble billions of dollars on a black box. So, we use <strong>SHAP (SHapley Additive exPlanations)</strong>—a tool that mathematically proves what factors forced the AI to make its prediction.</p>
                </div>
                <div class="flex-1 bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <img src="./images/04_shap_summary_plot.png" alt="SHAP Plot" class="w-full h-auto rounded-lg zoom-img" loading="lazy">
                    <div class="mt-4 text-sm text-slate-500 bg-slate-50 p-3 rounded-lg">
                        <strong class="text-slate-900">SHAP Insight:</strong> Look at the top rows. The SHAP graph tells us unequivocally: raw tariffs matter, but losing "Out-Degree Centrality" (the number of partners) is the fastest way to kill an industry's exports. 
                    </div>
                </div>
            </div>
        </section>

        <hr class="border-slate-200">

        <!-- GNN -->
        <section>
             <div class="bg-pink-50 text-pink-800 text-sm font-bold uppercase tracking-widest px-3 py-1 rounded inline-block mb-4">Phase 3: The Physics of Trade</div>
            <h2 class="text-3xl font-bold mb-4">3. Graph Neural Networks (GNN)</h2>
            <p class="text-slate-600 mb-6">We map every country, industry, and route into a giant 3D spiderweb. If an industry loses a trade route, how far does it get physically ripped away from the center of the web? We call this calculation "L2 Positional Embedding Shift."</p>
            
            <figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm mb-6 max-w-2xl mx-auto">
                <img src="./images/gnn_shock_propagation.png" alt="GNN Propagation" class="w-full h-auto rounded-lg zoom-img" loading="lazy">
                <figcaption class="mt-4 text-sm text-slate-500 bg-slate-50 p-4 rounded-lg">
                    <strong class="text-slate-900">What this proves:</strong> High-edge sectors like Auto and Pharma undergo severe shifts in the network (bars reaching to the right). They are literally forced off the global value chain axis. It's a structural failure, not just a temporary dip in profits.
                </figcaption>
            </figure>
        </section>

        <div class="text-center pt-8">
            <a href="policy_engine.html" class="inline-block bg-slate-900 text-white font-bold py-4 px-8 rounded-xl hover:bg-slate-800 transition">Next: The Autonomous Policy Engine &rarr;</a>
        </div>

    </main>
""" + footer_html

# PAGE 4: POLICY ENGINE
policy_content = head_html.format(title="Autonomous Policy Engine | AI Policy Simulation", nav=nav_html) + """
    <header class="bg-emerald-900 text-white py-16">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h1 class="text-4xl font-extrabold mb-4">Fixing the Future</h1>
            <p class="text-xl text-emerald-200">Causal Forests and Reinforcement Learning determining the ultimate strategy.</p>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-16 space-y-20">
        
        <!-- Causal Forests -->
        <section>
            <div class="text-center mb-10">
                <h2 class="text-3xl font-bold mb-4">Solving Research Question 2: Testing Treatments</h2>
                <p class="text-lg text-slate-600 max-w-2xl mx-auto">Before we deploy an AI to run the country's economy, we must independently verify if the tools the government has actually work. We used <strong>Causal Forests</strong> to find the Average Treatment Effect (ATE).</p>
            </div>

            <div class="grid md:grid-cols-2 gap-8 mb-8">
                <div class="bg-amber-50 p-8 rounded-2xl border border-amber-200 shadow-sm">
                    <h3 class="text-2xl font-bold text-amber-900 mb-2">Option A: Subsidies</h3>
                    <p class="text-amber-800 mb-6">Throwing cash grants (like PLI schemes) at domestic factories to temporarily lower prices.</p>
                    <div class="text-4xl font-black text-amber-600 mb-2">19.5 <span class="text-lg font-normal">ATE</span></div>
                    <p class="text-sm font-bold text-amber-900">Result: Fails.</p>
                    <p class="text-sm text-amber-800 mt-2">Cash provides localized relief but completely fails to rebuild broken international transit routes. When money runs out, the sector dies anyway.</p>
                </div>

                <div class="bg-emerald-50 p-8 rounded-2xl border border-emerald-200 shadow-sm">
                    <h3 class="text-2xl font-bold text-emerald-900 mb-2">Option B: Draft New Treaties</h3>
                    <p class="text-emerald-800 mb-6">Forging Alternative FTAs with other developing nations (e.g., ASEAN, UAE) to rebuild the broken hubs.</p>
                    <div class="text-4xl font-black text-emerald-600 mb-2">75.1 <span class="text-lg font-normal">ATE</span></div>
                    <p class="text-sm font-bold text-emerald-900">Result: Massive Success.</p>
                    <p class="text-sm text-emerald-800 mt-2">This manually solders new global network bridges. It mathematically restores structural elasticity.</p>
                </div>
            </div>
            
            <div class="text-center">
                 <img src="./images/08_causal_treatment_effect.png" alt="Causal Treatment Effects" class="w-full max-w-2xl mx-auto rounded-lg shadow-md zoom-img" loading="lazy">
                 <p class="mt-4 text-sm text-slate-500">Visual mapping of the vast disparity in causal recovery effectiveness.</p>
            </div>
        </section>

        <hr class="border-slate-200">

        <!-- RL -->
        <section class="bg-slate-900 text-white p-8 md:p-12 rounded-3xl shadow-xl">
            <h2 class="text-3xl font-extrabold mb-6">The AI Boss: Reinforcement Learning (RL) Engine</h2>
            <p class="text-slate-300 text-lg mb-8 leading-relaxed">
                Knowing what works isn't enough; when managing an economy over 10 years with a strict budget, timing is everything. We trained an autonomous <strong>Proximal Policy Optimization (PPO)</strong> Agent. The agent plays the role of the government. Its goal: get export volumes back up without bankrupting the treasury.
            </p>

            <div class="grid md:grid-cols-2 gap-8">
                <div>
                     <img src="./images/05_rl_volume_trajectory.png" alt="RL Volume Trajectory" class="w-full h-auto rounded-xl zoom-img border border-slate-700" loading="lazy">
                     <p class="mt-3 text-sm text-slate-400"><strong>The Save:</strong> The agent successfully halts the crash (red curve) and actively re-accelerates output year-over-year into positive territory (blue curve).</p>
                </div>
                <div>
                     <img src="./images/06_rl_policy_distribution.png" alt="RL Policy Selection" class="w-full h-auto rounded-xl zoom-img border border-slate-700" loading="lazy">
                     <p class="mt-3 text-sm text-slate-400"><strong>The Decisions:</strong> Removing human bias, the AI discovers that maximizing long-term survival requires heavily prioritizing 'Alt FTAs' directly over raw cash subsidies.</p>
                </div>
            </div>
        </section>

        <!-- Conclusion -->
        <section class="mb-16">
            <h2 class="text-3xl font-extrabold text-slate-900 mb-8 border-b-2 border-slate-200 pb-4">Final Conclusion</h2>
            <div class="prose prose-lg text-slate-700 max-w-none">
                <p>This project proves that the damage from major global trade shocks is <strong>structural, not just financial</strong>.</p>
                <p>When the system predicted massive drops using the <strong>XGBoost and LSTM</strong> engines, <strong>SHAP and Graph Neural Networks</strong> confirmed that the primary cause wasn't just "higher transport costs," but the literal fracturing of the "Out-Degree" network links connecting India to the west.</p>
                <p>Because the damage is structural—like a broken bridge—pumping money into factories (subsidies) does almost nothing to fix the long-term issue, as proven by our <strong>Causal Forest network</strong>. Finally, our <strong>Reinforcement Learning AI Engine</strong> successfully optimized a 10-year policy strategy outperforming human baselines, demonstrating that economic survival relies exclusively on aggressively seeking and drafting new treaties with alternative global partners.</p>
            </div>
        </section>

        <div class="text-center">
            <a href="index.html" class="text-blue-600 font-bold hover:underline">Return to Home</a>
        </div>

    </main>
""" + footer_html

with open('website/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
with open('website/data.html', 'w', encoding='utf-8') as f:
    f.write(data_content)
with open('website/ai_models.html', 'w', encoding='utf-8') as f:
    f.write(ai_content)
with open('website/policy_engine.html', 'w', encoding='utf-8') as f:
    f.write(policy_content)

print("Generated all files successfully.")
