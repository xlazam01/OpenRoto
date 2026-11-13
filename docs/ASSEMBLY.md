# Assembly

How to put one OpenRoto together. Item numbers match the [BOM](BOM.md) and the exploded view
(telescope side up). What each part does is in [`PARTS.md`](PARTS.md).

![OpenRoto exploded view](openroto_exploded.png)

> The CAD draws the outer ring (4a, milled) and the GT2 sleeve (4b, printed) as one body. In the real
> rotator they are two parts: the printed sleeve is pressed over the outer ring's rim.

## Tools and supplies

- Hex key 1.5 mm (screws 6; usually also the grub screws of the pulley 7)
- Calipers
- Fine abrasive paper (240 → 400 grit) for fitting the bearing pocket, and isopropyl alcohol to clean
- Optional: torque screwdriver (0.3–0.5 N·m range), low-strength threadlocker (blue) for the pulley grub screws

## Before you start

- Clean all parts; blow the chips and blasting media out of the tapped holes of the outer ring.
- **Check the bearing fits** (JLCCNC does not hold a defined precision fit):
  - Bearing 5 on the inner ring 1: the RAU5005 should slide onto the Ø50 seat by hand, without play.
    On the first build this fit was fine as delivered.
  - Bearing 5 in the outer ring 4a: the RAU5005's outer ring should go into the Ø61 pocket snugly,
    pushed in with even thumb pressure. On the first build the pocket was too tight: sand the pocket
    wall evenly (paper on a round former, turning the ring, re-trying often) until it fits. Stop as
    soon as it goes in: too loose lets the bearing shift. Clean off all dust.
- Never press on the bearing's inner ring to push its outer ring (or the other way round): the
  crossed rollers take the force and can dent the races.

## Steps

1. **GT2 sleeve onto the outer ring.** Press the printed sleeve 4b over the outer ring's rim, belt
   flange towards the outer ring's flange side, until it seats all round. It is held by friction.
2. **Bearing onto the inner ring.** Slide the bearing 5 onto the inner ring 1's Ø50 seat from the
   thread side until it touches the Ø52 flange. Push on the bearing's inner ring only.
3. **Spacer.** Slide the spacer ring 2 onto the seat behind the bearing, lip towards the bearing.
4. **Into the outer ring.** Lower the inner ring with the bearing into the outer ring 4a, so the
   bearing's outer ring sits in the Ø61 pocket. Push on the bearing's outer ring only.
5. **Clamp ring.** Put the clamp ring 3 on top, spigot into the outer ring, countersinks up. Line up
   the six holes with the tapped holes.
6. **Screws.** Turn in all six screws 6 by hand first. Then tighten them in a star pattern
   (1-4-2-5-3-6) in two rounds: first just touching, then **snug, about 0.3–0.5 N·m** — firm with the
   short arm of the 1.5 mm key, not with the long arm. M2.5 threads in aluminium strip easily; the screws
   only clamp the bearing's outer ring, they carry no torque.
7. **First check.** Hold the clamp ring and turn the inner ring: it must turn smoothly all round with
   no tight spots. A tight spot means the outer ring is clamped unevenly (loosen all six, retighten in
   the star pattern) or the pocket is still too tight.
8. **Into the imaging train.** Screw the flattener (or other telescope-side part) into the clamp
   ring's female M48. Screw the OAG (or the next part) onto the inner ring's male M48 until it bears on
   the spacer: this clamps the bearing's inner ring. Snug by hand.
9. **Motor and pulley.** Fix the pulley 7 on the motor 9 shaft (a grub screw on the shaft flat, a drop
   of blue threadlocker) so its teeth line up with the sleeve's teeth. Mount the motor on its mount
   (in Triton: the OpenWheel motor housing + slotted plate) with the slots loose.
10. **Belt.** Lay the belt 8 over the sleeve and the pulley. Slide the motor away from the rotator
    until the belt is taut and tighten the mount screws. **Tension:** pressed with one finger in the
    middle of the long span, the belt should give about 2–3 mm. Too loose skips teeth when the train
    is heavy; too tight loads the motor bearings and wears the printed teeth. Nominal centre distance
    is 97.90 mm (the mount allows 93.8–98.7 mm).

## Final check

- **Turns freely:** with the motor unpowered, the camera side turns by hand (through the 10:1 drive)
  without tight spots over a full turn.
- **No play:** hold the telescope side and rock the camera side axially and sideways — no knock or
  movement may be felt. If there is, the next part is not screwed down onto the spacer (step 8) or the
  bearing pocket was sanded too far.
- **Belt tracks:** run a full turn with the motor (32 000 steps at 16 µsteps; 88.889 steps/°). The
  belt stays on the sleeve's flange, does not climb the pulley flanges and does not skip.
- **Back to the start:** after +360° and −360° the rotator returns to its mark (no lost steps).
