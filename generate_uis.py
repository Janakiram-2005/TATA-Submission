import os

base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car UI - {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
        #toast {{ position: fixed; top: 40px; left: 50%; transform: translateX(-50%); background: #10b981; color: white; padding: 15px 30px; border-radius: 30px; display: none; font-weight: bold; z-index: 50; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .interactive {{ cursor: pointer; transition: all 0.2s; }}
        .interactive:hover {{ filter: brightness(1.2); transform: scale(1.02); }}
        .interactive:active {{ transform: scale(0.95); }}
    </style>
</head>
<body>
    <div id="toast">Action Registered!</div>
    
    <button onclick="runAutoTest()" class="fixed top-4 right-4 bg-purple-600 hover:bg-purple-500 text-white font-bold py-2 px-4 rounded-full shadow-lg z-50 transition-all flex items-center gap-2 border-2 border-purple-400">
        <span>🤖</span> Auto Test UI
    </button>
    
    <div class="w-full max-w-5xl {container_classes}">
        <!-- Dashboard Header -->
        <div class="flex justify-between items-center mb-6 {header_display}">
            <h1 class="text-2xl font-bold text-cyan-400">{title}</h1>
            <div class="flex gap-4 text-sm font-mono text-slate-400">
                <span>10:42 AM</span>
                <span>72°F Outside</span>
                <span>5G LTE</span>
            </div>
        </div>

        <!-- Main UI -->
        {content}
    </div>

    <script>
        function showToast(msg) {{
            let t = document.getElementById('toast');
            t.innerText = "✅ " + msg;
            t.style.display = 'block';
            setTimeout(() => t.style.display = 'none', 2000);
        }}

        async function runAutoTest() {{
            const elements = document.querySelectorAll('.interactive');
            const btn = document.querySelector('button[onclick="runAutoTest()"]');
            btn.innerHTML = '<span>⏳</span> Testing...';
            btn.disabled = true;
            
            for (let i = 0; i < elements.length; i++) {{
                const el = elements[i];
                // Highlight
                const originalOutline = el.style.outline;
                const originalTransform = el.style.transform;
                el.style.outline = '4px solid #a855f7';
                el.style.outlineOffset = '2px';
                el.style.transform = 'scale(1.05)';
                el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                
                await new Promise(r => setTimeout(r, 500));
                
                // Simulate click
                el.click();
                
                await new Promise(r => setTimeout(r, 1200));
                
                // Restore
                el.style.outline = originalOutline;
                el.style.transform = originalTransform;
                await new Promise(r => setTimeout(r, 300));
            }}
            
            btn.innerHTML = '<span>✅</span> Test Complete';
            setTimeout(() => {{
                btn.innerHTML = '<span>🤖</span> Auto Test UI';
                btn.disabled = false;
            }}, 3000);
        }}
    </script>
</body>
</html>
"""

uis = [
    {
        "filename": "car_ui_1_premium_touch.html",
        "title": "Premium Touch Interface",
        "container_classes": "bg-slate-900 border border-slate-700 p-8 rounded-3xl shadow-2xl",
        "header_display": "",
        "content": """
        <div class="grid grid-cols-12 gap-6 h-[600px]">
            <!-- Navigation -->
            <div class="col-span-8 bg-slate-800 rounded-2xl p-6 relative overflow-hidden flex flex-col justify-between interactive" onclick="showToast('Opened Full Map')">
                <div class="relative z-10 flex justify-between items-start">
                    <div>
                        <h2 class="text-xl font-bold text-white mb-1">San Francisco Airport</h2>
                        <p class="text-cyan-400 font-mono text-sm">ETA: 24 min (18.4 mi)</p>
                    </div>
                    <div class="bg-cyan-500 text-black px-4 py-2 rounded-full font-bold text-sm">Route</div>
                </div>
                <div class="relative z-10 mt-auto bg-slate-900/80 p-4 rounded-xl backdrop-blur-md inline-block w-fit">
                    <p class="text-slate-300 text-sm font-mono">Next Turn</p>
                    <p class="font-bold text-lg text-white">Bear right onto US-101 S</p>
                </div>
                <!-- Fake Map Background -->
                <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] bg-cyan-900"></div>
            </div>
            
            <!-- Media & Climate -->
            <div class="col-span-4 flex flex-col gap-6">
                <!-- Media -->
                <div class="bg-slate-800 rounded-2xl p-6 flex-1 interactive flex flex-col justify-center" onclick="showToast('Toggled Play/Pause')">
                    <p class="text-xs text-indigo-400 font-mono mb-2 uppercase">Now Playing</p>
                    <h3 class="font-bold text-lg text-white truncate">Midnight City</h3>
                    <p class="text-slate-400 text-sm mb-4">M83</p>
                    <div class="w-full bg-slate-700 h-2 rounded-full mb-4">
                        <div class="bg-cyan-400 h-2 rounded-full" style="width: 45%"></div>
                    </div>
                    <div class="flex justify-between items-center text-slate-300">
                        <span class="text-xl font-black">⏮</span>
                        <span class="text-4xl font-black text-cyan-400">⏸</span>
                        <span class="text-xl font-black">⏭</span>
                    </div>
                </div>
                
                <!-- Climate -->
                <div class="bg-slate-800 rounded-2xl p-6 flex-1 interactive" onclick="showToast('Adjusted Driver Temperature')">
                    <p class="text-xs text-teal-400 font-mono mb-2 uppercase">Climate Zone</p>
                    <div class="flex justify-between items-center h-full">
                        <div class="text-center">
                            <p class="text-4xl font-bold text-white mb-1">70°</p>
                            <p class="text-xs text-slate-400 font-mono">Driver</p>
                        </div>
                        <div class="text-3xl text-slate-600">|</div>
                        <div class="text-center">
                            <p class="text-4xl font-bold text-white mb-1">72°</p>
                            <p class="text-xs text-slate-400 font-mono">Pass</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    {
        "filename": "car_ui_2_budget_touch.html",
        "title": "Budget Touch Display",
        "container_classes": "bg-slate-800 border-4 border-slate-900 p-6 rounded-xl shadow-lg max-w-3xl w-full",
        "header_display": "",
        "content": """
        <div class="grid grid-cols-2 gap-4 h-[400px]">
            <div class="bg-slate-700 rounded-lg p-6 flex flex-col items-center justify-center interactive" onclick="showToast('Radio Station Changed')">
                <div class="text-6xl mb-4">📻</div>
                <h3 class="text-xl font-bold text-white mb-2">FM 104.5</h3>
                <p class="text-slate-400">Pop Radio</p>
            </div>
            <div class="bg-slate-700 rounded-lg p-6 flex flex-col items-center justify-center interactive" onclick="showToast('Bluetooth Paired')">
                <div class="text-6xl mb-4">📱</div>
                <h3 class="text-xl font-bold text-white mb-2">My iPhone</h3>
                <p class="text-emerald-400">Connected</p>
            </div>
            <div class="col-span-2 bg-slate-900 rounded-lg p-4 flex justify-between items-center">
                <div class="px-6 py-3 bg-slate-700 rounded-md text-white font-bold interactive" onclick="showToast('Menu Opened')">MENU</div>
                <div class="px-6 py-3 bg-slate-700 rounded-md text-white font-bold interactive" onclick="showToast('Nav Opened')">NAV</div>
                <div class="px-6 py-3 bg-slate-700 rounded-md text-white font-bold interactive" onclick="showToast('Media Opened')">MEDIA</div>
                <div class="px-6 py-3 bg-slate-700 rounded-md text-white font-bold interactive" onclick="showToast('Phone Opened')">TEL</div>
            </div>
        </div>
        """
    },
    {
        "filename": "car_ui_3_premium_hybrid.html",
        "title": "Premium Hybrid (Touch + Buttons)",
        "container_classes": "bg-slate-900 border border-slate-700 p-8 rounded-3xl shadow-2xl",
        "header_display": "",
        "content": """
        <div class="flex flex-col gap-6 h-[650px]">
            <!-- Touch Screen Component -->
            <div class="h-[400px] bg-slate-800 rounded-2xl p-6 border-b-4 border-cyan-500 flex items-center justify-center interactive" onclick="showToast('Map Interaction')">
                <div class="text-center">
                    <div class="text-6xl mb-4">🗺️</div>
                    <h2 class="text-2xl font-bold text-white">Navigation Active</h2>
                    <p class="text-cyan-400 mt-2">12 mins to Destination</p>
                </div>
            </div>
            
            <!-- Physical Button Simulation -->
            <div class="flex-1 bg-gradient-to-b from-slate-800 to-slate-900 rounded-2xl p-6 grid grid-cols-4 gap-4">
                <div class="bg-slate-950 rounded-xl border border-slate-700 flex flex-col items-center justify-center interactive shadow-inner" onclick="showToast('AC Toggled')">
                    <span class="text-2xl mb-2 text-blue-400">❄️</span>
                    <span class="text-xs font-mono font-bold text-slate-300">A/C MAX</span>
                </div>
                <div class="bg-slate-950 rounded-xl border border-slate-700 flex flex-col items-center justify-center interactive shadow-inner" onclick="showToast('Fan Speed Increased')">
                    <span class="text-2xl mb-2 text-white">💨</span>
                    <span class="text-xs font-mono font-bold text-slate-300">FAN SPEED</span>
                </div>
                <div class="bg-slate-950 rounded-xl border border-slate-700 flex flex-col items-center justify-center interactive shadow-inner" onclick="showToast('Defrost Active')">
                    <span class="text-2xl mb-2 text-orange-400">♨️</span>
                    <span class="text-xs font-mono font-bold text-slate-300">DEFROST</span>
                </div>
                <div class="bg-slate-950 rounded-xl border border-slate-700 flex flex-col items-center justify-center interactive shadow-inner" onclick="showToast('Auto Mode On')">
                    <span class="text-2xl mb-2 text-emerald-400">⚡</span>
                    <span class="text-xs font-mono font-bold text-slate-300">AUTO</span>
                </div>
            </div>
        </div>
        """
    },
    {
        "filename": "car_ui_4_budget_hybrid.html",
        "title": "Budget Hybrid (Screen + Knobs)",
        "container_classes": "bg-slate-800 border border-slate-900 p-6 rounded-xl shadow-lg max-w-3xl w-full",
        "header_display": "",
        "content": """
        <div class="flex flex-col gap-8">
            <!-- Basic Display -->
            <div class="h-[250px] bg-blue-900/40 border-2 border-blue-500/50 rounded-lg flex items-center justify-center interactive" onclick="showToast('Track Skipped')">
                <div class="text-center text-blue-100">
                    <p class="text-sm font-mono mb-2">Track 04 / USB</p>
                    <h2 class="text-3xl font-bold mb-4">Hotel California</h2>
                    <div class="flex gap-4 justify-center text-xl">
                        <span>⏪</span><span>▶️</span><span>⏩</span>
                    </div>
                </div>
            </div>
            
            <!-- Rotary Knobs Row -->
            <div class="flex justify-around items-center bg-slate-900 p-6 rounded-lg">
                <div class="w-24 h-24 rounded-full bg-slate-700 border-4 border-slate-600 shadow-xl flex items-center justify-center interactive" onclick="showToast('Volume Changed')">
                    <span class="text-slate-300 font-bold text-xs uppercase">Vol</span>
                </div>
                <div class="grid grid-cols-3 gap-2">
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 1')">1</button>
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 2')">2</button>
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 3')">3</button>
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 4')">4</button>
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 5')">5</button>
                    <button class="bg-slate-700 text-white font-bold p-3 rounded shadow interactive" onclick="showToast('Preset 6')">6</button>
                </div>
                <div class="w-24 h-24 rounded-full bg-slate-700 border-4 border-slate-600 shadow-xl flex items-center justify-center interactive" onclick="showToast('Tuning Changed')">
                    <span class="text-slate-300 font-bold text-xs uppercase">Tune</span>
                </div>
            </div>
        </div>
        """
    },
    {
        "filename": "car_ui_5_premium_button.html",
        "title": "Premium Button-First Design",
        "container_classes": "bg-[#111827] border-2 border-slate-800 p-8 rounded-3xl",
        "header_display": "hidden",
        "content": """
        <!-- Central non-touch display surrounded by premium physical buttons -->
        <div class="grid grid-cols-12 gap-8 h-[600px] items-center">
            <!-- Left Button Bank -->
            <div class="col-span-2 flex flex-col gap-4">
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Nav Button Pressed')">NAV</div>
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Media Button Pressed')">MEDIA</div>
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Radio Button Pressed')">RADIO</div>
            </div>
            
            <!-- Central Display (Non-Touch visual indicator) -->
            <div class="col-span-8 bg-black h-full rounded-2xl border-4 border-slate-900 flex flex-col overflow-hidden relative shadow-[inset_0_0_50px_rgba(0,0,0,1)]">
                <div class="bg-slate-900 p-4 border-b border-slate-800 flex justify-between text-slate-400 font-mono text-xs">
                    <span>10:42 AM</span>
                    <span>No Phone Connected</span>
                    <span>72°F</span>
                </div>
                <div class="flex-1 flex flex-col items-center justify-center text-center p-8">
                    <div class="text-6xl text-cyan-500 mb-6">🎙️</div>
                    <h2 class="text-2xl font-bold text-white mb-2">Voice Assistant Active</h2>
                    <p class="text-slate-400">"Navigate to 123 Main Street..."</p>
                    
                    <!-- Audio visualization bars -->
                    <div class="flex gap-2 mt-8 h-12 items-end">
                        <div class="w-3 bg-cyan-500 h-full rounded-t"></div>
                        <div class="w-3 bg-cyan-500 h-2/3 rounded-t"></div>
                        <div class="w-3 bg-cyan-500 h-4/5 rounded-t"></div>
                        <div class="w-3 bg-cyan-500 h-1/2 rounded-t"></div>
                        <div class="w-3 bg-cyan-500 h-full rounded-t"></div>
                    </div>
                </div>
            </div>
            
            <!-- Right Button Bank -->
            <div class="col-span-2 flex flex-col gap-4">
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Tel Button Pressed')">TEL</div>
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Car Button Pressed')">CAR</div>
                <div class="bg-gradient-to-b from-slate-700 to-slate-800 text-white font-bold h-20 rounded-xl border border-slate-600 shadow-lg flex items-center justify-center interactive" onclick="showToast('Settings Button Pressed')">SET</div>
            </div>
        </div>
        """
    },
    {
        "filename": "car_ui_6_screenless.html",
        "title": "Screenless / Tactile Interface",
        "container_classes": "bg-stone-900 border-4 border-stone-800 p-10 rounded-[40px] shadow-2xl max-w-4xl w-full",
        "header_display": "hidden",
        "content": """
        <!-- Completely physical UI represented as HTML elements -->
        <h2 class="text-center text-stone-500 font-mono tracking-widest uppercase mb-10 text-sm">Center Console Tactile Array</h2>
        
        <div class="flex justify-between items-center px-10">
            <!-- Left Driver Knob -->
            <div class="relative w-32 h-32 rounded-full bg-gradient-to-tr from-stone-800 to-stone-700 border-8 border-stone-950 shadow-[0_10px_20px_rgba(0,0,0,0.5)] flex items-center justify-center interactive" onclick="showToast('Driver Temp Adjusted')">
                <div class="absolute -top-6 text-blue-400 font-bold">18°</div>
                <div class="absolute -bottom-6 text-red-400 font-bold">28°</div>
                <div class="w-16 h-16 rounded-full bg-stone-900 border border-stone-600 shadow-inner"></div>
                <!-- Indicator dot -->
                <div class="absolute top-2 left-6 w-3 h-3 bg-red-500 rounded-full shadow-[0_0_10px_red]"></div>
            </div>
            
            <!-- Center Buttons Row -->
            <div class="flex gap-4">
                <div class="w-16 h-24 bg-gradient-to-b from-stone-700 to-stone-800 rounded-lg border-2 border-stone-900 flex flex-col items-center justify-center interactive shadow-[0_5px_10px_rgba(0,0,0,0.5)]" onclick="showToast('Hazards Toggled')">
                    <div class="w-0 h-0 border-l-[10px] border-l-transparent border-b-[15px] border-b-red-500 border-r-[10px] border-r-transparent mb-1"></div>
                    <div class="w-0 h-0 border-l-[6px] border-l-transparent border-b-[9px] border-b-stone-900 border-r-[6px] border-r-transparent absolute mb-1"></div>
                </div>
                
                <div class="w-16 h-24 bg-gradient-to-b from-stone-700 to-stone-800 rounded-lg border-2 border-stone-900 flex flex-col items-center justify-center interactive shadow-[0_5px_10px_rgba(0,0,0,0.5)]" onclick="showToast('AC Toggled')">
                    <span class="text-stone-300 font-bold text-xs">A/C</span>
                </div>
                
                <div class="w-16 h-24 bg-gradient-to-b from-stone-700 to-stone-800 rounded-lg border-2 border-stone-900 flex flex-col items-center justify-center interactive shadow-[0_5px_10px_rgba(0,0,0,0.5)]" onclick="showToast('Recirculate Toggled')">
                    <span class="text-stone-300 text-2xl">↺</span>
                </div>
            </div>
            
            <!-- Right Pass Knob -->
            <div class="relative w-32 h-32 rounded-full bg-gradient-to-tr from-stone-800 to-stone-700 border-8 border-stone-950 shadow-[0_10px_20px_rgba(0,0,0,0.5)] flex items-center justify-center interactive" onclick="showToast('Pass Temp Adjusted')">
                <div class="absolute -top-6 text-blue-400 font-bold">18°</div>
                <div class="absolute -bottom-6 text-red-400 font-bold">28°</div>
                <div class="w-16 h-16 rounded-full bg-stone-900 border border-stone-600 shadow-inner"></div>
                <!-- Indicator dot -->
                <div class="absolute top-2 right-6 w-3 h-3 bg-blue-500 rounded-full shadow-[0_0_10px_blue]"></div>
            </div>
        </div>
        
        <div class="mt-16 flex justify-center">
            <!-- Large Media Control Dial -->
            <div class="relative w-48 h-48 rounded-full bg-gradient-to-tr from-stone-700 to-stone-600 border-[12px] border-stone-900 shadow-[0_15px_30px_rgba(0,0,0,0.6)] flex items-center justify-center interactive" onclick="showToast('Media Dial Turned')">
                <div class="w-24 h-24 rounded-full bg-stone-900 flex items-center justify-center border-4 border-stone-800 interactive" onclick="event.stopPropagation(); showToast('Media Dial Pressed')">
                    <span class="text-stone-400 font-bold text-sm">OK</span>
                </div>
                
                <!-- Direction arrows -->
                <span class="absolute top-4 text-stone-400 text-xl">▲</span>
                <span class="absolute bottom-4 text-stone-400 text-xl">▼</span>
                <span class="absolute left-4 text-stone-400 text-xl">◀</span>
                <span class="absolute right-4 text-stone-400 text-xl">▶</span>
            </div>
        </div>
        """
    }
]

for ui in uis:
    html = base_template.format(
        title=ui["title"],
        container_classes=ui["container_classes"],
        header_display=ui["header_display"],
        content=ui["content"]
    )
    with open(ui["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {ui['filename']}")
