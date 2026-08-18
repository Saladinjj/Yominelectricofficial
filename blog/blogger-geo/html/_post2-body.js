(() => { const cmEl = document.querySelector(".CodeMirror"); if (!cmEl || !cmEl.CodeMirror) return {err: "no codemirror"}; const cm = cmEl.CodeMirror; cm.setValue(`<p><strong>Short answer:</strong> Size a voltage stabilizer by adding up the running watts of every load you need to protect, multiplying by a 1.25–1.5 safety margin (motors and compressors draw 3–6x their running current at startup), then converting watts to VA (divide by the power factor, typically 0.8). A 5 kVA stabilizer protects roughly 4 kW of running load; when in doubt, step up one size.</p>
<h2>Why sizing matters more than brand</h2>
<p>Voltage sags are the most expensive power-quality problem in industry — analysis of industrial facilities shows sags and swells create cascading costs that organizations typically underestimate, and more than 60% of power-quality costs are attributed to voltage sags alone. One published study put the average annual cost of voltage sags for an industrial consumer at US$64,417.</p>
<p>An undersized stabilizer trips under load and drops the very equipment it was meant to protect. An oversized one wastes capital and runs at poor efficiency. Correct sizing is the difference between a stabilizer that pays for itself and one that becomes another maintenance ticket.</p>
<h2>The three numbers you need</h2>
<h3>1. Total running load (watts)</h3>
<p>List every device the stabilizer must feed, read each nameplate's wattage (or V × A × power factor), and sum them. Do not include loads you can leave unprotected.</p>
<h3>2. Startup surge</h3>
<p>Motors, compressors, and refrigerators draw 3–6x running current for a few seconds at start. If your total running load is 3 kW but includes a 2 kW compressor, the stabilizer must absorb the startup peak of that compressor on top of other loads — this is where undersized stabilizers fail.</p>
<h3>3. VA rating and power factor</h3>
<p>Stabilizers are rated in VA/kVA. Convert watts to VA: VA = watts ÷ power factor (use 0.8 if unknown). Then apply the safety margin:</p>
<p><strong>Sizing formula:</strong></p>
<blockquote>Stabilizer kVA = (total running watts ÷ power factor) × 1.25</blockquote>
<p><strong>Example:</strong> 3,000 W of running load ÷ 0.8 = 3,750 VA × 1.25 = 4,687 VA → buy a 5 kVA stabilizer.</p>
<h2>Sizing table for common installations</h2>
<table>
<tr><th>Application</th><th>Typical running load</th><th>Recommended stabilizer</th></tr>
<tr><td>Single refrigerator + TV + lights</td><td>500–800 W</td><td>1–1.5 kVA</td></tr>
<tr><td>Small shop (fans, PC, mini fridge)</td><td>1.5–2 kW</td><td>2.5–3 kVA</td></tr>
<tr><td>Home/office (AC 1.5HP + appliances)</td><td>3–4 kW</td><td>5 kVA</td></tr>
<tr><td>Small clinic or restaurant kitchen</td><td>5–6 kW</td><td>7.5–8 kVA</td></tr>
<tr><td>Industrial control panel / CNC</td><td>8–12 kW</td><td>12–15 kVA</td></tr>
<tr><td>Three-phase production line</td><td>20–40 kW</td><td>25–50 kVA (3-phase)</td></tr>
</table>
<h2>Servo vs relay stabilizers: pick by accuracy need</h2>
<table>
<tr><th>Feature</th><th>Servo (servo-motor)</th><th>Relay (buck-boost)</th></tr>
<tr><td>Output accuracy</td><td>±0.5% to ±1%</td><td>±3% to ±6%</td></tr>
<tr><td>Response speed</td><td>1–2 seconds</td><td>0.1–0.5 seconds</td></tr>
<tr><td>Best for</td><td>Sensitive medical/industrial equipment</td><td>General appliances</td></tr>
<tr><td>Cost</td><td>Higher</td><td>Lower</td></tr>
</table>
<p>For CNC machines, lab instruments, and imaging equipment, specify a servo stabilizer at ±0.5–1% accuracy. For household and general commercial loads, a relay type at ±3–6% is usually sufficient and far cheaper.</p>
<h2>Common sizing mistakes</h2>
<p>1. <strong>Forgetting startup current</strong> — the #1 cause of "my stabilizer keeps tripping." 2. <strong>Sizing for nameplate kVA instead of actual load</strong> — nameplates are worst-case; actual draw is often lower, so use measured or realistic load. 3. <strong>Skipping the power factor</strong> — mixing watts and VA directly under-sizes the unit by up to 25%. 4. <strong>Ignoring the voltage range</strong> — a stabilizer rated for 140–260 V input cannot hold output if your grid sags below its design window. Match the input range to your actual grid conditions. 5. <strong>One stabilizer for mixed-sensitivity loads</strong> — don't feed a CNC machine and a water heater from the same unit; the heater's switching will cause output hunting on the servo.</p>
<h2>FAQ: Voltage stabilizer sizing</h2>
<p><strong>Q: How do I calculate the kVA I need for my stabilizer?</strong> A: Sum the running watts of all protected loads, divide by the power factor (0.8 if unknown), multiply by 1.25 for startup margin. Example: 4,000 W ÷ 0.8 × 1.25 = 6,250 VA → choose 7.5 kVA.</p>
<p><strong>Q: What happens if my stabilizer is too small?</strong> A: It trips on overload or drops output voltage under load, leaving equipment unprotected — often exactly when a sag hits.</p>
<p><strong>Q: Can I oversize a voltage stabilizer?</strong> A: Yes, oversizing by 25–50% is safe and common practice; it only costs a little more and gives headroom for future loads. Undersizing is the real risk.</p>
<p><strong>Q: What size stabilizer do I need for a 1.5-ton air conditioner?</strong> A: A 1.5-ton AC draws roughly 1.5–2 kW running with a startup spike near 6 kW. Most installers size it at 3–5 kVA depending on other loads on the same unit.</p>
<p><strong>Q: Servo or relay stabilizer — which should I choose?</strong> A: If your equipment is sensitive (CNC, medical, lab, printing), choose servo at ±0.5–1% accuracy. For household appliances and general commercial loads, relay type at ±3–6% is sufficient and budget-friendly.</p>
<p><strong>Q: Do I need a three-phase stabilizer for a three-phase machine?</strong> A: Yes. Feed a three-phase machine with a matched three-phase stabilizer (3× single-phase sizing), and verify the connection is star or delta as your site requires.</p>
<p><strong>Q: What input voltage range should I look for?</strong> A: Measure your grid's actual low and high extremes across a week. Choose a stabilizer whose input window covers them — e.g., 140–260 V for unstable networks, 190–250 V for reasonably stable ones.</p>
<h2>Conclusion</h2>
<p>Sizing a voltage stabilizer is a five-minute calculation that prevents years of downtime: total running watts ÷ power factor × 1.25, rounded up, with the input range matched to your grid and the technology (servo vs relay) matched to your load sensitivity. When in doubt between two sizes, take the larger — the cost difference is small, and the protection difference is not.</p>
<p>Yomin Electric has manufactured servo and relay <a href="https://www.yominelectric.com/products?category=voltage-stabilizer-regulator" rel="noopener" target="_blank">voltage stabilizers</a> since 1996, with factory-direct pricing and technical support for importers, distributors, and project engineers. <a href="https://www.yominelectric.com/contact.html" rel="noopener" target="_blank">Send your load list and grid voltage data</a> and the engineering team will confirm the exact model and kVA.</p>
<h2>Sources</h2>
<ul>
<li>MDPI Energies, "Cost of Industrial Process Shutdowns Due to Voltage Sag" (2021)</li>
<li>OrteaNext, "Voltage sag: the most critical of all power quality issues"</li>
<li>Delta Wye, "Main Causes of Voltage Sags and Swells Explained" — analysis of 500+ industrial facilities</li>
</ul>`); cm.save(); const hta = document.querySelector("textarea.Fdco1c"); if (hta) hta.dispatchEvent(new Event("input", {bubbles:true})); return {len: cm.getValue().length, head: cm.getValue().slice(0,60)}; })()