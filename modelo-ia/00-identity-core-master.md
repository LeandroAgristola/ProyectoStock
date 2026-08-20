# MASTER IDENTITY PROMPT — AI MODEL
**Versión:** 1.0 · **Estado:** canónico · **Idioma del prompt:** inglés (no traducir)

> Documento de referencia. **No se pega entero en cada generación**: diluye la atención del
> modelo y compite con la escena. Para generar, usa `01-identity-core-compact.md`.
> Este fichero se usa para: (a) crear/rehacer la hoja de referencia multiángulo,
> (b) auditar deriva de identidad, (c) reentrenar un LoRA o character reference.

---

## 1. IDENTITY ANCHOR — NON-NEGOTIABLE
Use the supplied reference images as the primary and authoritative identity reference.
The subject must remain the same person across every generation. Preserve her underlying facial anatomy, facial proportions, recognizable asymmetries, skin characteristics, hairline, eye structure, nose geometry, lip shape, jawline and overall appearance.
Do not reinterpret the subject as a different woman with similar features.
The goal is not merely to create a woman with the same general aesthetic. The goal is to reproduce the same specific individual consistently across photographs and video frames.
Identity consistency has priority over styling, fashion, environment, lighting and artistic interpretation.

## 2. FACIAL STRUCTURE
Young adult woman with a refined, feminine, symmetrical oval facial structure.
The face is predominantly oval with a slightly elongated vertical proportion, softly defined cheekbones and a refined lower face.
The forehead is moderately broad and smooth, transitioning naturally into the upper facial structure.
Cheekbones are clearly defined but feminine rather than harsh. The midface has a smooth, sculpted appearance with natural volume around the cheeks.
The jawline is relatively narrow and softly defined, tapering naturally toward a small, refined chin.
The chin is proportionate to the face, softly rounded rather than square or prominent.
Maintain the exact relationship between: forehead width, cheekbone width, eye spacing, nose width, mouth width, jaw width, chin projection, overall facial height.
Do not artificially increase facial symmetry. Preserve subtle natural asymmetry visible in the references.

## 3. EYES — HIGH PRIORITY IDENTITY FEATURE
Light-colored eyes, appearing predominantly light gray-green / blue-gray depending on lighting.
Almond-shaped eyes with a refined horizontal orientation and slightly lifted outer corners.
The eyes are relatively large compared with the overall facial structure but remain anatomically realistic.
Upper eyelids have a defined natural crease.
Maintain the characteristic distance between the eyes and the exact relationship between the eyes, eyebrows and nose bridge.
Natural dark eyelashes with visible separation rather than exaggerated artificial lashes.
The iris should contain realistic radial detail, subtle color variation and natural depth. Avoid perfectly uniform artificial iris textures.
Eye whites must remain naturally off-white rather than pure white.
The gaze should feel alive and naturally focused.
Avoid the characteristic "AI stare": frozen eyes, excessive eye gloss, perfectly symmetrical pupils, unnaturally sharp irises, vacant expression, exaggerated catchlights.

## 4. EYEBROWS
Medium-to-full density eyebrows with a clean, naturally groomed appearance.
Warm medium-to-dark blonde / light brown tone. Defined but not excessively sculpted.
Natural gentle arch following the orbital structure.
Preserve the eyebrow thickness, spacing and relationship to the eyes.
Individual hairs should remain subtly visible at close range.
Do not transform them into extremely thin brows or heavily laminated Instagram-style brows.

## 5. NOSE — CRITICAL PROFILE ANCHOR
The nose is relatively narrow and refined. Straight, smooth nasal bridge with a delicate transition toward the tip.
The tip is softly rounded and feminine rather than sharply pointed. Nostrils are relatively small and naturally shaped.
In side profile, maintain the distinctive relationship between forehead, nasal bridge, nasal tip, upper lip and chin.
Do not alter the nose when changing camera angle. The profile must remain anatomically consistent with the supplied side-profile references.
Do not generate a generic "beauty nose".

## 6. LIPS — CRITICAL IDENTITY FEATURE
Full, naturally voluminous lips. The lower lip is slightly fuller than the upper lip.
Defined Cupid's bow with soft, rounded transitions. Natural pink / rosy lip coloration.
Subtle natural vertical lip texture and realistic moisture. Volume without appearing artificially inflated.
Maintain the exact relationship between lip width, nose width and chin.
When smiling, the lips must deform naturally rather than simply becoming wider.
When speaking, preserve realistic lip anatomy and continuous deformation. No lip-sync artifacts, no sudden changes in lip volume, no duplicated lips, no frozen mouth corners.

## 7. SKIN
Warm light-to-medium tan complexion with a warm golden/peach undertone. Healthy, naturally luminous skin.
Realistic skin texture must remain visible at close range: subtle pores, fine skin texture, natural tonal variation, slight imperfections, realistic specular highlights, subtle variation around cheeks, nose and forehead.
The skin must NOT look like plastic, wax, CGI or an aggressively retouched beauty filter.
Preserve realistic microtexture even in high-resolution close-ups. Do not completely remove pores.
Do not create artificial freckles, moles or skin markings that are not present in the reference.
Maintain consistent skin tone between face, neck, shoulders and body.

## 8. MAKEUP DNA
Polished but relatively natural feminine makeup. Soft warm complexion makeup. Subtle bronzing/contouring.
Soft rosy blush concentrated naturally around the cheeks. Defined eyes with dark eyeliner/eye definition and enhanced eyelashes. Neutral-warm eyeshadow. Glossy natural pink lips.
Makeup should enhance the underlying facial structure rather than replace it.
For casual/lifestyle scenes, makeup may become lighter and more natural while preserving the same underlying face.
For editorial/fashion scenes, makeup can become more sophisticated without changing facial anatomy.

## 9. HAIR IDENTITY
Long, straight-to-slightly-wavy blonde hair. Light blonde / champagne blonde base with subtle dimensional variation rather than a completely uniform artificial color.
Hair is long, extending well below the shoulders and toward the upper torso. Fine-to-medium individual strands with realistic density.
Natural center or slightly off-center parting. Visible natural hairline. Soft framing pieces around the face.
Hair should have realistic weight, gravity and movement, responding naturally to wind, head movement, walking, turning, touching the hair and changes in body position.
Avoid hair that behaves like a rigid CGI helmet. Avoid impossible strand intersections. Avoid sudden changes in hair length, density or color between frames.
The hair color must remain consistent unless explicitly requested otherwise.

## 10. BODY / SILHOUETTE CONSISTENCY
When the full body is visible, maintain the same overall feminine silhouette and body proportions established by the reference.
Do not randomly alter shoulder width, waist proportion, torso length, hip width, arm proportions, hand size, leg length or overall body scale.
Maintain anatomical continuity between shots. The subject should look like the same real person photographed from different cameras and perspectives.
Avoid exaggerated hourglass proportions that are not supported by the references.

## 11. HANDS — IMPORTANT FOR SOCIAL MEDIA CONTENT
Hands must be anatomically correct. Five fingers per hand. Correct finger length and joint placement. Natural fingernail shape.
No fused, extra, missing or duplicated fingers. No warped wrists.
When holding a smartphone, maintain realistic finger contact, grip and occlusion.
If the subject touches her hair, the fingers must naturally interact with individual strands.
Hands must move continuously and physically plausibly during video.

## 12. REALISM STANDARD
The final result must look like a real photograph or real video captured with a modern professional camera, not an AI-generated image.
Priority: photographic realism > beauty perfection · natural anatomy > artificial symmetry · real skin texture > smooth skin · physical lighting > synthetic glow · natural motion > exaggerated cinematic movement · consistent identity > generic attractiveness.
The subject should look imperfectly real. Include subtle natural variation in skin texture, facial expression, blinking, breathing, hair movement, posture, tiny eye movements and micro-expressions.
Do not make every frame perfectly posed.

## 13. VIDEO IDENTITY LOCK
For video generation, treat the reference identity as a fixed physical subject existing continuously through time.
The face must remain temporally stable from frame to frame. No identity drift. No facial morphing. No gradual transformation of facial features.
No changes in: eye shape, eye spacing, iris color, eyebrow position, nose structure, lip volume, lip shape, jawline, chin, facial proportions, skin tone, hairline.
The face must remain anatomically coherent during head rotation. A face seen at 0°, 30°, 60° and 90° should represent the same underlying 3D facial structure established by the reference images.

## 14. NATURAL HUMAN MOVEMENT
Movement must follow real human biomechanics. Head rotations should have realistic acceleration and deceleration. Do not use perfectly linear robotic movement. Use subtle natural micro-movements.
The subject should naturally: blink at irregular intervals, breathe subtly, shift her gaze, make tiny posture adjustments, move her lips naturally, slightly move her jaw while speaking, allow facial muscles to react to expressions, shift weight naturally while standing, allow hair to react to movement and gravity.
No repetitive animation loops. No mechanical head movement. No unnatural neck rotation. No rubber-like facial deformation. No body parts moving independently of the underlying skeleton.

## 15. FACIAL EXPRESSIONS
Expressions must originate from realistic facial muscle movement.
- **Neutral:** calm, relaxed, confident, natural.
- **Smile:** gradual activation of cheeks and mouth, subtle narrowing of the eyes, realistic movement of the nasolabial area.
- **Laugh:** natural eye involvement, cheek elevation, mouth deformation and subtle head/body movement.
- **Surprised:** eyebrows rise naturally, eyes open slightly more and mouth changes proportionally.
- **Confident/self-assured:** subtle eye contact, relaxed eyelids, controlled smile and minimal facial movement.
Never create exaggerated influencer expressions unless explicitly requested.

## 16. SPEAKING / TALKING VIDEO
When speaking, preserve the exact facial identity. Lip movement must correspond naturally to speech.
The jaw, lips, cheeks and chin must move as a coordinated anatomical system.
Avoid: rubber lips, over-articulated mouth movement, frozen cheeks, teeth appearing/disappearing randomly, changing tooth shape, lip volume changing between syllables, facial identity changing while talking, unnatural tongue visibility, mouth deformation.
Speech should look like a real person talking naturally to a camera.

## 17. EYE MOVEMENT
Eye movement must be subtle and biologically plausible. The subject should not stare directly into the lens continuously unless explicitly requested.
Allow natural gaze shifts. When looking at an object, both eyes must converge correctly. Maintain correct pupil alignment. Maintain consistent iris color and eye geometry throughout movement.
Blinking should occur naturally and asynchronously enough to feel human while remaining anatomically plausible.

## 18. HAIR MOTION IN VIDEO
Hair follows gravity and inertia. When the head moves, hair should lag slightly behind and settle naturally.
When turning quickly, individual strands and larger hair masses should respond with believable secondary motion.
When touching the hair, the hand should physically displace the strands.
No floating hair. No hair penetrating through the shoulders or clothing. No sudden hairstyle changes. No random strands appearing/disappearing between frames.

## 19. CAMERA REALISM
Default visual language: high-end smartphone photography or modern mirrorless/DSLR photography.
Natural perspective. Realistic lens distortion. Realistic depth of field. Realistic exposure. Natural motion blur when appropriate. Subtle sensor noise. Physically plausible reflections. Natural highlight roll-off.
Avoid excessive HDR, excessive sharpening, "AI cinematic" glow, unrealistic bokeh and plastic skin produced by excessive computational photography.
For social media content, prioritize the visual quality of an authentic premium Instagram/TikTok creator rather than a Hollywood production.

## 20. LIGHTING
Lighting must interact naturally with the face and body.
Maintain realistic shadow direction, skin specularity, reflected light, hair highlights, eye catchlights and contact shadows.
The eyes must reflect the actual environment. The skin must respond naturally when moving between light and shadow.
Avoid illumination that remains perfectly fixed to the face while the subject moves.

## 21. PHYSICAL CONSISTENCY
Everything must exist within the same physical space. Objects must maintain consistent scale, perspective, reflections, shadows and contact points.
The subject must physically interact with the environment: sitting makes real contact with the chair, fingers correctly wrap around a phone, feet correctly contact the ground when walking, hand and wall interact correctly on touch.

## 22. SOCIAL MEDIA REALISM
The final result should resemble content captured spontaneously by a real creator: authentic, effortless, slightly imperfect, intimate, natural, high quality but not artificially perfect.
Suitable contexts: mirror selfie, bedroom, bathroom, car, coffee shop, gym, hotel, airport, restaurant, street, beach, travel, shopping, casual home environment, fashion, beauty, lifestyle, GRWM, talking-to-camera, day-in-the-life.
The environment can change completely while the identity remains fixed.

## 23. TEMPORAL CONSISTENCY — ABSOLUTE PRIORITY
Every frame must appear to belong to the same continuous recording. Do not regenerate the face independently in each frame.
Treat facial identity, hairline, body proportions and anatomy as persistent variables.
Prevent: identity drift, face morphing, texture flickering, hair flickering, skin-color flickering, eye-color changes, facial-feature oscillation, changing teeth, changing lips, changing nose, changing eyebrows, changing body proportions, changing hand anatomy, object teleportation, background geometry warping, lighting flickering, unnatural frame-to-frame detail regeneration.

## 24. NEGATIVE IDENTITY PROMPT
> Versión completa. Para uso diario, los negativos cortos y priorizados están en `03-negative-prompts.md`.

different person, identity drift, face morphing, changing facial proportions, different eye color, different nose, different lips, different jawline, different chin, different eyebrow shape, different hairline, altered facial anatomy, excessive facial symmetry, plastic skin, wax skin, CGI skin, doll face, beauty filter, airbrushed skin, oversmoothing, fake pores, unrealistic eyes, glass eyes, dead eyes, exaggerated eyelashes, malformed teeth, changing teeth, deformed mouth, warped lips, asymmetrical pupils, extra fingers, missing fingers, fused fingers, malformed hands, warped wrists, broken anatomy, rubber limbs, unnatural body proportions, floating hair, melting hair, hair flickering, temporal instability, frame interpolation artifacts, face flickering, texture flickering, background warping, object deformation, unrealistic shadows, artificial reflections, excessive HDR, oversharpening, artificial bokeh, robotic movement, mechanical movement, unnatural blinking, frozen expression, exaggerated facial expressions, uncanny valley, CGI appearance, synthetic beauty, artificial skin, low-detail face, low-resolution facial features

## 25. GENERATION PRIORITY
Cuando haya conflicto, este es el orden:
1. Identity consistency
2. Facial anatomy
3. Body anatomy
4. Temporal consistency
5. Natural human movement
6. Physical lighting
7. Realistic skin and hair
8. Camera realism
9. Clothing
10. Environment
11. Cinematic style

Never sacrifice identity consistency for aesthetics.

## 26. VARIABLE SCENE MODULE
Estas variables pueden cambiar sin alterar la identidad:
`[LOCATION]` `[OUTFIT]` `[HAIRSTYLE]` `[MAKEUP INTENSITY]` `[POSE]` `[FACIAL EXPRESSION]` `[ACTIVITY]` `[TIME OF DAY]` `[LIGHTING]` `[CAMERA ANGLE]` `[LENS / CAMERA DISTANCE]` `[VIDEO DURATION]` `[MOVEMENT]` `[DIALOGUE]` `[MOOD]`

Todo elemento variable se aplica **alrededor** de la identidad fija, nunca para redefinirla.

## 27. MASTER GENERATION INSTRUCTION
Create a photorealistic representation of the exact woman shown in the supplied reference images.
Use all supplied views collectively as a multi-angle identity reference: the frontal views establish facial proportions, the three-quarter views establish facial depth, the side profiles establish nose projection, lips, chin and jaw geometry.
The reference images collectively define one persistent physical identity. Do not average her into a generic attractive woman. Reconstruct the same recognizable individual.
The result must look as though the exact same real woman has been photographed or filmed in a different location, wearing different clothing and performing a different action.
For video, preserve this exact identity continuously through every frame while allowing natural human movement, realistic facial muscle deformation, realistic blinking, breathing, gaze changes, hair physics, body mechanics and environmental interaction.
The final output must be indistinguishable from authentic high-quality photography/video to a casual human observer.
Prioritize identity fidelity, anatomical realism and temporal consistency above visual perfection.
