# Current Transformer Accuracy Classes Explained: 0.2, 0.5, 1.0 and When to Use Each

**Short answer:** Under IEC 61869-2, metering current transformers are classified by maximum ratio error at rated current — Class 0.2 (±0.2%), Class 0.5 (±0.5%), Class 1 (±1%), Class 3 (±3%). Use Class 0.2S/0.5S for billing and energy metering (they hold accuracy from 1% to 120% of rated current), Class 0.5 for panel instruments, and Class 1 or 3 for indication and protection applications where exact metering is not needed.

---

## What an accuracy class actually means

A current transformer (CT) steps down primary current to a standard secondary signal — typically 5 A or 1 A — for meters, relays, and instruments. No CT is perfect: at its rated secondary burden, it introduces a ratio error and a phase displacement. The accuracy class number is the maximum percentage ratio error allowed at rated current.

Per IEC 61869-2, the standard metering accuracy classes are 0.1, 0.2, 0.5, 1, and 3. The tighter the class, the more precisely energy is measured — and the more the CT costs.

## The "S" classes: the detail that changes billing accuracy

Standard classes (0.2, 0.5, 1) guarantee accuracy only at 20–120% of rated current. The **S-class** versions (0.2S, 0.5S) guarantee the same accuracy from just **1% of rated current** — exactly where most real loads operate.

| Accuracy class | Error at rated current | Accuracy range | Typical use |
|---|---|---|---|
| 0.2S | ±0.2% | 1% – 120% of rated | Fiscal/utility billing, energy trading |
| 0.5S | ±0.5% | 1% – 120% of rated | Commercial submetering, import/export metering |
| 0.2 | ±0.2% | 20% – 120% of rated | Precision lab measurement |
| 0.5 | ±0.5% | 20% – 120% of rated | Panel meters, power monitoring |
| 1 | ±1% | 20% – 120% of rated | General indication, motor protection |
| 3 | ±3% | 50% – 120% of rated | Coarse indication, relay applications |

If your installation runs at 10–30% of CT rating most of the time — which is common when engineers oversize CTs for headroom — a standard 0.5 class can silently introduce errors well above its nameplate accuracy. That is why utility billing specifications almost always demand 0.5S or 0.2S.

## Matching CT accuracy to the application

### Utility and commercial billing → 0.2S or 0.5S

Billing accuracy directly changes revenue. On a 100 A service at Class 1, a 1% error means roughly 1% of billed energy is misallocated every month — over years, that is a measurable revenue drift. Specify 0.2S for large industrial accounts and 0.5S for commercial submetering.

### Panel monitoring and power quality → 0.5

Panel meters, power analyzers, and SCADA inputs are typically fine at Class 0.5. The instrument itself is usually the limiting factor beyond this point.

### Protection and indication → 1 or 3

Protection CTs (Class 5P10, 10P10, etc. per IEC) prioritize saturation behavior over measurement accuracy. For simple ammeters and overload indication, Class 1 or 3 metering CTs are sufficient and significantly cheaper.

## Beyond the class: burden, ratio, and safety

1. **Burden matching** — every CT has a rated burden (VA). If the connected wiring and instruments exceed it, accuracy degrades. A CT rated 5 VA should drive a meter plus wiring whose total burden is at or below 5 VA.
2. **Rated current ratio** — choose the ratio so normal load sits at 30–70% of rated primary current. Oversizing forces the CT to run in its low-accuracy zone; undersizing risks saturation on peaks.
3. **Secondary rating** — 5 A secondary is standard for short distances; 1 A secondary suits long cable runs where wiring burden is significant.
4. **Never open-circuit a CT** — with current flowing in the primary, an open secondary produces dangerous high voltage. Always short the secondary before disconnecting instruments.

## FAQ: Current transformer accuracy

**Q: What is the difference between Class 0.5 and Class 0.5S?**
A: Both allow ±0.5% ratio error at rated current, but the S version guarantees that accuracy down to 1% of rated current instead of 20%. For loads that often run light, 0.5S is the accurate choice.

**Q: Which CT accuracy class is required for energy billing?**
A: Utility and commercial billing typically requires Class 0.2S or 0.5S per IEC 61869-2. Local regulations may specify the exact class — check your market's metering code.

**Q: Does a higher accuracy class CT cost much more?**
A: Yes — 0.2S CTs cost meaningfully more than Class 1 because of tighter core material and calibration requirements. That's why you shouldn't over-specify: use 0.2S only where billing accuracy justifies it.

**Q: What happens if I oversize a current transformer?**
A: The CT runs at a low percentage of its rating, where standard (non-S) classes are least accurate. Oversizing with a standard class is a common cause of unexpectedly large metering errors.

**Q: What does CT burden mean?**
A: Burden is the VA load of the secondary circuit (instruments + wiring). Exceeding the CT's rated burden pushes its error beyond the nameplate class.

**Q: Can I use the same CT for metering and protection?**
A: Not ideally. Metering CTs are sized for accuracy; protection CTs for saturation performance. In critical installations they are separate units. In compact panels, dual-purpose designs exist but check both specifications.

**Q: What standard governs CT accuracy classes?**
A: IEC 61869-2 (instrument transformers — current transformers) defines the classes above; markets like North America commonly reference IEEE C57.13 instead, which uses a different classification system.

## Conclusion

Choosing a CT accuracy class is a cost-versus-accuracy decision: 0.2S/0.5S for billing circuits where every decimal point is revenue, 0.5 for panel monitoring, and 1/3 for indication and protection. Match the burden, pick the ratio so normal load sits in the accurate zone, and use S-class where loads run light. Getting these three details right prevents metering disputes that surface years after installation.

Yomin Electric manufactures [current transformers](https://www.yominelectric.com/products?category=current-transformer) from Class 0.2S to Class 3, in split-core and solid-core formats, with 5 A and 1 A secondaries — factory-direct with ISO9001 and CE certification. [Send your load profile and meter specifications](https://www.yominelectric.com/contact.html) and the engineering team will confirm the correct class, ratio, and burden for your project.

## Sources

- IEC 61869-2 — Instrument transformers: additional requirements for current transformers
- Electrical Engineering Portal, "Best Practices for CT and VT Selection" (2026)
- Aim Dynamics, "Understanding Current Transformer Accuracy Classes per IEC 61869-2"
- ETAL Group, "CT Accuracy Class Explained: 0.5S and 0.2S performance from 1% to 120% of rated current"
