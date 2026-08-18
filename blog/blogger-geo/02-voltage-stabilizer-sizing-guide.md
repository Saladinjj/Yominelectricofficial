# Voltage Stabilizer Sizing Guide: How to Pick the Right kVA for Your Equipment

**Short answer:** Size a voltage stabilizer by adding up the running watts of every load you need to protect, multiplying by a 1.25–1.5 safety margin (motors and compressors draw 3–6x their running current at startup), then converting watts to VA (divide by the power factor, typically 0.8). A 5 kVA stabilizer protects roughly 4 kW of running load; when in doubt, step up one size.

---

## Why sizing matters more than brand

Voltage sags are the most expensive power-quality problem in industry — analysis of industrial facilities shows sags and swells create cascading costs that organizations typically underestimate, and more than 60% of power-quality costs are attributed to voltage sags alone. One published study put the average annual cost of voltage sags for an industrial consumer at US$64,417.

An undersized stabilizer trips under load and drops the very equipment it was meant to protect. An oversized one wastes capital and runs at poor efficiency. Correct sizing is the difference between a stabilizer that pays for itself and one that becomes another maintenance ticket.

## The three numbers you need

### 1. Total running load (watts)

List every device the stabilizer must feed, read each nameplate's wattage (or V × A × power factor), and sum them. Do not include loads you can leave unprotected.

### 2. Startup surge

Motors, compressors, and refrigerators draw 3–6x running current for a few seconds at start. If your total running load is 3 kW but includes a 2 kW compressor, the stabilizer must absorb the startup peak of that compressor on top of other loads — this is where undersized stabilizers fail.

### 3. VA rating and power factor

Stabilizers are rated in VA/kVA. Convert watts to VA: VA = watts ÷ power factor (use 0.8 if unknown). Then apply the safety margin:

**Sizing formula:**
> Stabilizer kVA = (total running watts ÷ power factor) × 1.25

**Example:** 3,000 W of running load ÷ 0.8 = 3,750 VA × 1.25 = 4,687 VA → buy a 5 kVA stabilizer.

## Sizing table for common installations

| Application | Typical running load | Recommended stabilizer |
|---|---|---|
| Single refrigerator + TV + lights | 500–800 W | 1–1.5 kVA |
| Small shop (fans, PC, mini fridge) | 1.5–2 kW | 2.5–3 kVA |
| Home/office (AC 1.5HP + appliances) | 3–4 kW | 5 kVA |
| Small clinic or restaurant kitchen | 5–6 kW | 7.5–8 kVA |
| Industrial control panel / CNC | 8–12 kW | 12–15 kVA |
| Three-phase production line | 20–40 kW | 25–50 kVA (3-phase) |

## Servo vs relay stabilizers: pick by accuracy need

| Feature | Servo (servo-motor) | Relay (buck-boost) |
|---|---|---|
| Output accuracy | ±0.5% to ±1% | ±3% to ±6% |
| Response speed | 1–2 seconds | 0.1–0.5 seconds |
| Best for | Sensitive medical/industrial equipment | General appliances |
| Cost | Higher | Lower |

For CNC machines, lab instruments, and imaging equipment, specify a servo stabilizer at ±0.5–1% accuracy. For household and general commercial loads, a relay type at ±3–6% is usually sufficient and far cheaper.

## Common sizing mistakes

1. **Forgetting startup current** — the #1 cause of "my stabilizer keeps tripping."
2. **Sizing for nameplate kVA instead of actual load** — nameplates are worst-case; actual draw is often lower, so use measured or realistic load.
3. **Skipping the power factor** — mixing watts and VA directly under-sizes the unit by up to 25%.
4. **Ignoring the voltage range** — a stabilizer rated for 140–260 V input cannot hold output if your grid sags below its design window. Match the input range to your actual grid conditions.
5. **One stabilizer for mixed-sensitivity loads** — don't feed a CNC machine and a water heater from the same unit; the heater's switching will cause output hunting on the servo.

## FAQ: Voltage stabilizer sizing

**Q: How do I calculate the kVA I need for my stabilizer?**
A: Sum the running watts of all protected loads, divide by the power factor (0.8 if unknown), multiply by 1.25 for startup margin. Example: 4,000 W ÷ 0.8 × 1.25 = 6,250 VA → choose 7.5 kVA.

**Q: What happens if my stabilizer is too small?**
A: It trips on overload or drops output voltage under load, leaving equipment unprotected — often exactly when a sag hits.

**Q: Can I oversize a voltage stabilizer?**
A: Yes, oversizing by 25–50% is safe and common practice; it only costs a little more and gives headroom for future loads. Undersizing is the real risk.

**Q: What size stabilizer do I need for a 1.5-ton air conditioner?**
A: A 1.5-ton AC draws roughly 1.5–2 kW running with a startup spike near 6 kW. Most installers size it at 3–5 kVA depending on other loads on the same unit.

**Q: Servo or relay stabilizer — which should I choose?**
A: If your equipment is sensitive (CNC, medical, lab, printing), choose servo at ±0.5–1% accuracy. For household appliances and general commercial loads, relay type at ±3–6% is sufficient and budget-friendly.

**Q: Do I need a three-phase stabilizer for a three-phase machine?**
A: Yes. Feed a three-phase machine with a matched three-phase stabilizer (3× single-phase sizing), and verify the connection is star or delta as your site requires.

**Q: What input voltage range should I look for?**
A: Measure your grid's actual low and high extremes across a week. Choose a stabilizer whose input window covers them — e.g., 140–260 V for unstable networks, 190–250 V for reasonably stable ones.

## Conclusion

Sizing a voltage stabilizer is a five-minute calculation that prevents years of downtime: total running watts ÷ power factor × 1.25, rounded up, with the input range matched to your grid and the technology (servo vs relay) matched to your load sensitivity. When in doubt between two sizes, take the larger — the cost difference is small, and the protection difference is not.

Yomin Electric has manufactured servo and relay [voltage stabilizers](https://www.yominelectric.com/products?category=voltage-stabilizer-regulator) since 1996, with factory-direct pricing and technical support for importers, distributors, and project engineers. [Send your load list and grid voltage data](https://www.yominelectric.com/contact.html) and the engineering team will confirm the exact model and kVA.

## Sources

- MDPI Energies, "Cost of Industrial Process Shutdowns Due to Voltage Sag" (2021)
- OrteaNext, "Voltage sag: the most critical of all power quality issues"
- Delta Wye, "Main Causes of Voltage Sags and Swells Explained" — analysis of 500+ industrial facilities
