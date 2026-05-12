#!/usr/bin/env python3
"""Generate an-psychoeducation.html with AN_PE_GROUPS for use by gen_psychoeducation.py."""

def esc(s):
    return s.replace("'", "\\'")

groups = [
    {
        "label": None,
        "optional": False,
        "items": [
            {
                "id": "what_an_is",
                "title": "What anorexia nervosa is — and what it is not",
                "body": """<p><strong>The defining features:</strong> Anorexia nervosa is characterised by persistent restriction of energy intake leading to significantly low body weight, an intense fear of gaining weight or persistent behaviour that interferes with weight gain, and a disturbance in the way weight or body shape is experienced — either distorted perception, excessive influence on self-evaluation, or lack of recognition of the seriousness of low weight.</p>
<p><strong>What it is not:</strong></p>
<ul>
<li>A diet that went too far</li>
<li>Vanity or an obsession with appearance</li>
<li>A choice or a lifestyle preference</li>
<li>A condition that only affects young women</li>
<li>Something you can simply decide to recover from if you want it enough</li>
</ul>
<p><strong>The medical severity:</strong> Anorexia nervosa has the highest mortality rate of any psychiatric condition — approximately 5–10% of people with AN will die from the illness, and a significant proportion of deaths are from suicide rather than medical complications alone. This is not stated to frighten — it is stated because the seriousness is often underestimated by both patients and those around them, and because it matters for treatment decisions.</p>
<p><strong>Two subtypes:</strong></p>
<ul>
<li><strong>Restricting type:</strong> Weight loss achieved primarily through restriction and exercise, without regular binge-purge episodes</li>
<li><strong>Binge-purge type:</strong> Regular binge eating or purging behaviour (self-induced vomiting, laxatives, diuretics) in addition to overall restriction. Not the same as bulimia nervosa, which does not involve the same degree of weight suppression and different psychopathology.</li>
</ul>
<p><strong>Who develops AN:</strong> Approximately 1% of women and 0.3% of men meet full criteria at some point in their lifetime, with substantially higher rates of subclinical presentations. AN occurs across all demographics, socioeconomic groups, and body types. Rates in male, transgender, and older populations are significantly under-detected. The typical age of onset is adolescence to early adulthood, though late-onset AN is not rare.</p>
<p><strong>A high genetic loading:</strong> Heritability estimates for AN are 50–80% — comparable to schizophrenia and higher than most personality disorders. AN is not caused by family, media, or culture in isolation. These factors modulate expression and course, but the biological substrate is real and significant. This matters because it removes blame and informs realistic treatment expectations.</p>"""
            },
            {
                "id": "brain_on_starvation",
                "title": "What starvation does to the brain — why logic does not work",
                "body": """<p><strong>The Minnesota Starvation Experiment (1944–1945):</strong> Thirty-six healthy, psychologically normal male volunteers were semi-starved over 24 weeks. What followed was not merely weight loss. They developed obsessional preoccupation with food, dramatically altered eating behaviours, food rituals, hoarding, social withdrawal, emotional dysregulation, depression, and — critically — distorted body image. These men did not have anorexia nervosa before the study. The starvation produced features that are clinically indistinguishable from AN. This is not an analogy. It is a demonstration of what malnutrition does to the human brain.</p>
<p><strong>What the starved brain does differently:</strong></p>
<ul>
<li><strong>Cognitive rigidity:</strong> The ability to think flexibly, consider alternatives, and update beliefs based on evidence is significantly impaired. Thinking becomes narrow, black-and-white, and repetitive. The brain defaults to familiar patterns rather than new ones.</li>
<li><strong>Reward processing:</strong> The brain's response to reward — including food — is abnormal in starvation. Restriction becomes less aversive and food becomes more frightening, not less, as malnutrition progresses. This is the opposite of what would be expected in normal physiology.</li>
<li><strong>Serotonin:</strong> Serotonin synthesis requires dietary tryptophan. Restriction of protein intake reduces serotonin availability, which impairs mood regulation, increases anxiety, and contributes to obsessional thinking — all of which may paradoxically be temporarily relieved by further restriction.</li>
<li><strong>Body image perception:</strong> Brain regions involved in body image perception (right parietal cortex, insula) are directly affected by malnutrition. The distorted body image in AN is not purely psychological — it has a neurological substrate that cannot be corrected by logic alone and improves substantially with nutritional rehabilitation.</li>
<li><strong>Threat sensitivity:</strong> The malnourished brain is a high-threat, low-flexibility brain. Everything feels more dangerous, uncertainty is intolerable, and the known (restriction) feels safer than the unknown (recovery) even when recovery is objectively necessary.</li>
</ul>
<p><strong>The critical implication:</strong> You cannot think your way out of anorexia while malnourished, and neither can your therapist think you out of it. Nutritional rehabilitation is not the end of treatment — it is the prerequisite for treatment to be possible. This is not a moral failing; it is neuroscience. The brain that needs to participate in recovery is the same brain that starvation has impaired.</p>"""
            },
            {
                "id": "ego_syntonic",
                "title": "Ego-syntonic illness — why AN feels like identity, not illness",
                "body": """<p><strong>What ego-syntonic means:</strong> Unlike most psychiatric conditions — where symptoms feel alien and unwanted (ego-dystonic) — anorexia nervosa is typically experienced as consistent with the self, valued, and in some way desired. The illness does not feel like OCD feels (foreign, intrusive, distressing), or like depression feels (heavy, unwanted). It feels like control, identity, achievement, and safety.</p>
<p><strong>What AN can provide that makes it hard to give up:</strong></p>
<ul>
<li>A sense of control in a life that feels uncontrollable</li>
<li>A clear, definable identity: "I am someone who does not eat like other people"</li>
<li>A way to manage overwhelming emotions without having to feel them</li>
<li>A sense of achievement and competence measured through restriction</li>
<li>A way to communicate distress without words</li>
<li>Protection from feared experiences (puberty, intimacy, adulthood, scrutiny, failure)</li>
<li>Temporary relief from anxiety through control and predictability</li>
</ul>
<p><strong>Why this matters for treatment:</strong> If AN is providing something genuinely valuable — even something that is destroying your health — then "just eat" is not only unhelpful, it is tone-deaf to the function the illness is serving. Effective treatment addresses what the restriction is doing for you, not just that restriction is occurring. Recovery means finding alternative ways to feel safe, competent, and in control — not simply removing the primary strategy without offering anything in its place.</p>
<p><strong>The internal conflict:</strong> Most people with AN experience some degree of ambivalence. Part of the person wants to recover — to live fully, to have relationships, to eat with people, to not feel cold all the time. Part of the person is terrified of recovery and identifies with the illness. Both parts are real. Good treatment holds this ambivalence without demanding premature certainty about recovery and without colluding with the illness.</p>
<p><strong>What this does not mean:</strong> Ego-syntonic does not mean untreatable or hopeless. It means recovery requires a different approach than conditions where the person is unambiguously motivated to eliminate symptoms. Motivational engagement, externalising the illness, and building a valued life beyond AN are specific therapeutic skills for exactly this reason.</p>"""
            },
            {
                "id": "medical_complications",
                "title": "Medical complications — what malnutrition does to the body",
                "body": """<p><strong>Framing:</strong> The medical complications of anorexia nervosa are extensive and affect virtually every organ system. Many are reversible with nutritional rehabilitation; some are not. This is not comprehensive — it is intended as an overview for informed consent and shared understanding. All medical concerns should be discussed with your treating physician.</p>
<p><strong>Cardiac:</strong> The single most common cause of non-suicide mortality in AN. Malnutrition causes muscle loss including cardiac muscle — the heart literally shrinks. This produces bradycardia (slow heart rate), hypotension, and arrhythmias. Electrolyte abnormalities (particularly low potassium, magnesium, and phosphate) further increase arrhythmia risk. QTc prolongation on ECG indicates life-threatening rhythm risk. Cardiac complications can develop rapidly and without warning — they require regular monitoring.</p>
<p><strong>Refeeding syndrome:</strong> A potentially life-threatening complication of nutritional rehabilitation after prolonged starvation. When nutrition is introduced after severe restriction, shifts in phosphate, potassium, and magnesium cause cardiac arrhythmias, seizures, respiratory failure, and death if not managed. This is why nutritional rehabilitation must be medically supervised in severe presentations — not because eating is inherently dangerous, but because the reintroduction of nutrition after starvation requires careful monitoring.</p>
<p><strong>Bone density:</strong> Oestrogen suppression from low body weight causes accelerated bone loss. Bone density deficits in AN can be equivalent to osteoporosis in a young person, with fracture risk beginning well before older age. Bone density loss at low weight is not fully reversed by weight restoration — some loss is permanent. This has lifelong consequences.</p>
<p><strong>Brain:</strong> MRI studies consistently show grey matter volume reduction in AN. White matter tracts are affected. Cognitive impairment — particularly in flexibility, working memory, and sustained attention — is measurable and correlates with nutritional status. Much of this is reversible with weight restoration, though some structural changes may persist.</p>
<p><strong>Endocrine:</strong> Hypothalamic-pituitary-gonadal axis suppression causes amenorrhoea, loss of libido, and fertility impairment. Thyroid function is affected (low-T3 syndrome — the body conserves energy). Growth hormone resistance and insulin-like growth factor suppression affect growth in adolescents. Many of these normalise with nutritional rehabilitation but recovery is not always complete.</p>
<p><strong>Gastrointestinal:</strong> Gastric emptying slows significantly with restriction, causing early fullness, bloating, and nausea that are genuine physiological responses — not avoidance or exaggeration. This makes the early stages of nutritional rehabilitation particularly uncomfortable and requires realistic expectation-setting.</p>"""
            },
            {
                "id": "an_not_choice",
                "title": "What causes anorexia nervosa — beyond blame",
                "body": """<p><strong>AN is not caused by any single factor.</strong> It is a complex condition arising from the interaction of biological vulnerability, psychological factors, and environmental triggers. Understanding the genuine causes matters because it removes blame — from the person, from families, and from cultural explanations that are often overstated.</p>
<p><strong>Biological factors:</strong></p>
<ul>
<li><strong>Genetics:</strong> Twin studies show 50–80% heritability. Genome-wide association studies have identified shared genetic architecture with OCD, anxiety disorders, and metabolic traits. AN has both psychiatric and metabolic genetic contributions — it is not purely a psychological condition.</li>
<li><strong>Neurobiology:</strong> Altered dopamine and serotonin functioning, particularly in reward circuits and interoceptive processing. Abnormal response to food reward pre-dating illness onset has been documented. Heightened anxiety sensitivity and threat detection likely pre-date the illness.</li>
<li><strong>Temperament:</strong> High trait anxiety, perfectionism, harm avoidance, and obsessionality are consistent premorbid features — they appear before the eating disorder develops and are at least partly genetic in origin.</li>
</ul>
<p><strong>Psychological factors:</strong></p>
<ul>
<li>Perfectionism — particularly of the self-oriented and socially prescribed types</li>
<li>Low tolerance of uncertainty and need for control</li>
<li>Difficulties with emotion recognition and emotion regulation (alexithymia is common)</li>
<li>History of anxiety disorders (often precede AN)</li>
<li>Trauma history — particularly but not exclusively sexual trauma — increases risk but is not a prerequisite or a universal feature</li>
</ul>
<p><strong>Sociocultural factors:</strong> Western ideals of thinness create a cultural context in which AN symptoms are sometimes initially rewarded rather than treated. Media, diet culture, and social comparison provide the content for weight and shape concerns — but do not cause AN in the absence of biological and psychological vulnerability. Sociocultural factors are best understood as triggers and maintainers in vulnerable individuals, not as root causes in isolation.</p>
<p><strong>Families do not cause AN.</strong> A generation of research has failed to identify specific parenting styles or family dysfunction as causal. Families are typically the most important resource in recovery, particularly for adolescents. Blame directed at families is both inaccurate and counterproductive.</p>"""
            }
        ]
    },
    {
        "label": "Treatment",
        "optional": False,
        "items": [
            {
                "id": "an_treatment_overview",
                "title": "Treatment — what works and what the evidence actually shows",
                "body": """<p><strong>Honest framing:</strong> The evidence base for AN treatment is thinner than for most psychiatric conditions. This is partly because AN is comparatively rare, partly because randomised controlled trials in this population are methodologically difficult, and partly because severe presentations make random allocation to control conditions ethically problematic. This does not mean there is nothing to offer — it means the evidence must be interpreted carefully.</p>
<p><strong>What is consistently supported:</strong></p>
<ul>
<li><strong>For adolescents:</strong> Family-Based Treatment (FBT/Maudsley Approach) has the strongest evidence of any psychological treatment for adolescent AN, with recovery rates of 40–50% at 12 months and maintained improvement at 5-year follow-up. It is the recommended first-line treatment for adolescents.</li>
<li><strong>For adults:</strong> No single psychological treatment is clearly superior. Enhanced CBT (CBT-E), Specialist Supportive Clinical Management (SSCM), Focal Psychodynamic Therapy, and Cognitive Remediation Therapy (CRT) all have evidence. SSCM, which combines clinical management with a supportive therapeutic relationship, performs particularly well in head-to-head comparisons.</li>
<li><strong>Medical management:</strong> Essential in all moderate to severe presentations. Cannot be separated from psychological treatment — they are not alternatives but concurrent requirements.</li>
<li><strong>Higher levels of care:</strong> Inpatient and day program settings provide medical monitoring, structured nutrition, and intensive support when outpatient treatment is insufficient to achieve medical stability or meaningful progress.</li>
</ul>
<p><strong>What does not work:</strong></p>
<ul>
<li>Generic CBT not adapted for eating disorders</li>
<li>Non-directive supportive therapy as a primary modality</li>
<li>Purely motivational or insight-oriented therapy without attention to nutritional rehabilitation</li>
<li>Any approach that does not address weight restoration in presentations involving significantly low weight</li>
</ul>
<p><strong>Duration:</strong> AN treatment is long. Adult outpatient treatment typically spans 1–3 years. Recovery rates are meaningful but not uniform — approximately 50% achieve full recovery at long-term follow-up, 30% partial recovery, and a substantial minority follow a chronic course. Long-term outcomes are better than pessimistic clinical impressions suggest, but realistic timelines are necessary.</p>"""
            },
            {
                "id": "weight_restoration",
                "title": "Weight restoration — why it must come first",
                "body": """<p><strong>Weight restoration is not the goal of treatment.</strong> It is the prerequisite. This distinction is important. The goal is recovery — a full life, the ability to eat flexibly and without distress, freedom from the eating disorder. Weight restoration enables the brain to participate in the work that makes the rest of recovery possible.</p>
<p><strong>Why weight restoration must precede or accompany psychological work:</strong></p>
<ul>
<li>The malnourished brain cannot engage in the flexibility, insight, and emotional processing that psychological treatment requires — see the starvation neuroscience topic.</li>
<li>Cognitive distortions around weight and shape are directly maintained by malnutrition. Some "psychological" features of AN are better understood as starvation effects that resolve with nutrition — rigid thinking, obsessional preoccupation with food, emotional instability, distorted body perception.</li>
<li>Therapy sessions in which the person is severely malnourished are at best inefficient and at worst counterproductive — the content cannot be retained and processed in a starvation state.</li>
</ul>
<p><strong>What weight restoration involves:</strong> Gradual, supported, medically monitored increase in nutritional intake. The rate of restoration must be managed carefully to avoid refeeding syndrome (see medical complications). Supervised meal support — whether by family, dietitian, or clinical staff — is typically part of this process. A dietitian with eating disorder experience is an important team member.</p>
<p><strong>The experience of weight restoration:</strong> Uncomfortable. Physically, the refeeding process involves bloating, early fullness, nausea, oedema, constipation or rapid changes in bowel habit, and significant psychological distress. These symptoms are temporary and expected — they are physiological consequences of nutritional rehabilitation after restriction, not signs that something is going wrong or that the person is eating "too much." Realistic preparation for this experience significantly improves adherence.</p>
<p><strong>Weight overshoot:</strong> Some degree of weight redistribution and temporary overshoot before settling at a healthy set point is common and expected during recovery. The body prioritises fat restoration before lean mass restoration — this is an adaptive response and does not represent the final body composition. It is one of the most distressing aspects of early weight restoration and requires specific psychoeducation and support.</p>
<p><strong>What a healthy weight range means in practice:</strong> The weight at which the brain and body function normally — which is specific to the individual and cannot be determined in advance by charts alone. Menstrual function, bone density, cognitive function, and subjective wellbeing all provide indicators. Set point theory: the body defends a genetically determined weight range, and sustained restriction alters the set point over time, which is why recovery weights are sometimes higher than pre-illness weights and why ongoing restriction is required to maintain illness weight.</p>"""
            },
            {
                "id": "fbt",
                "title": "Family-Based Treatment (FBT/Maudsley) for adolescents",
                "body": """<p><strong>FBT is the most evidence-supported treatment for adolescent AN.</strong> Multiple randomised controlled trials and long-term follow-up studies support its efficacy, with approximately 40–50% achieving full remission at end of treatment and superior outcomes to individual therapy comparators at 12-month follow-up. It is recommended as first-line treatment by Australian, British, and American clinical guidelines.</p>
<p><strong>The core model:</strong> AN in adolescents is externalised — treated as something happening to the young person rather than as an expression of their personality or psychopathology. The parents are empowered to take temporary charge of nutritional rehabilitation, with the treatment team's guidance, until the adolescent has sufficient weight restoration to re-engage their own judgment about food and eating.</p>
<p><strong>Three phases of FBT:</strong></p>
<ul>
<li><strong>Phase 1 — Weight restoration:</strong> Parents take control of all food decisions. The therapeutic focus is on supporting parents in this role and managing the adolescent's distress, which is often intense. Family meals are rehearsed in session. The adolescent is not held responsible for their resistance — it is framed as the illness, not them.</li>
<li><strong>Phase 2 — Returning control:</strong> As weight is restored and the adolescent demonstrates emerging capacity for healthy eating decisions, age-appropriate control over eating is gradually returned, starting with less anxiety-provoking situations.</li>
<li><strong>Phase 3 — Establishing identity and independence:</strong> The focus shifts to adolescent developmental tasks — identity, independence, and the relational and psychological aspects of recovery beyond the eating disorder.</li>
</ul>
<p><strong>What FBT requires from families:</strong> Significant time, emotional energy, and the willingness to sit with their child's distress without backing down from the nutritional expectations. This is extraordinarily difficult. Parental guilt, self-blame, and exhaustion are common and should be directly addressed. Parental self-care is not a luxury — it is a clinical necessity for treatment adherence.</p>
<p><strong>Who FBT is not suitable for:</strong> Adults (different model applies), presentations where parental involvement is contraindicated, or families where the parent-adolescent dynamic cannot support the model. A trained FBT therapist makes this assessment individually.</p>"""
            },
            {
                "id": "adult_treatment",
                "title": "Treatment for adults — CBT-E, SSCM, and what to expect",
                "body": """<p><strong>CBT-E (Enhanced Cognitive Behavioural Therapy for Eating Disorders):</strong> Developed by Christopher Fairburn at Oxford. The most widely studied psychological treatment for adult AN. Addresses the "transdiagnostic" maintaining mechanisms of all eating disorders — the over-evaluation of eating, weight, and shape as a measure of self-worth — alongside AN-specific features including low weight and its consequences.</p>
<p><strong>CBT-E in practice:</strong></p>
<ul>
<li>Typically 40 sessions over 40 weeks for AN (longer than for normal-weight eating disorders)</li>
<li>Begins with psychoeducation and collaborative formulation of the maintaining mechanisms</li>
<li>Addresses weight regain alongside the psychological maintaining features simultaneously</li>
<li>Later addresses perfectionism, low self-esteem, and interpersonal difficulties that feed the eating disorder</li>
<li>Requires a motivated patient who can attend regularly and engage with between-session work — which is more difficult than standard CBT due to the cognitive effects of malnutrition</li>
</ul>
<p><strong>SSCM (Specialist Supportive Clinical Management):</strong> A less structured approach combining clinical management of weight (directiveness about nutrition and medical monitoring) with a supportive, non-confrontational therapeutic relationship. Particularly effective for people who find the structure of CBT aversive or who have difficulty engaging with formal psychological frameworks. Performs as well as or better than CBT-E in some comparisons despite being less theoretically elaborate.</p>
<p><strong>CRT (Cognitive Remediation Therapy):</strong> Targets the cognitive inflexibility and detail-focused processing style that characterises AN and is partly independent of nutritional status. Delivered as a precursor or adjunct to other treatments. Does not directly target eating-disorder cognition but improves the cognitive flexibility needed to engage in psychological treatment. Useful early in treatment or with chronic presentations.</p>
<p><strong>What "recovery" looks like for adults:</strong> Full recovery — normal weight, normalised eating, no eating disorder cognition, and good quality of life — occurs in approximately 50% of people at long-term follow-up (10–20 years). Partial recovery is more common. Chronic course affects a significant minority. These outcomes are better than commonly communicated in clinical settings, where pessimism about adult AN is often overstated.</p>"""
            },
            {
                "id": "medication_an",
                "title": "Medication in anorexia nervosa — an honest account",
                "body": """<p><strong>The frank picture:</strong> No medication is effective as a primary treatment for anorexia nervosa. This is one of the most striking facts about AN — conditions with comparable severity and chronicity typically have medication options that produce meaningful effects. AN does not, for reasons that include the neurobiological effects of malnutrition making pharmacological targets inaccessible.</p>
<table>
<thead><tr><th>Drug / Class</th><th>Evidence / Role</th><th>Considerations</th></tr></thead>
<tbody>
<tr><td><strong>SSRIs</strong><br>(fluoxetine, sertraline)</td><td>Do not facilitate weight restoration in underweight AN and do not improve eating-disorder cognition. Evidence for relapse prevention after weight restoration is mixed. Not recommended as primary treatment.</td><td>Serotonin synthesis requires dietary tryptophan — the malnourished brain lacks the substrate for SSRIs to act on. This is why they are ineffective at low weight. May have a role post-restoration for comorbid anxiety or depression.</td></tr>
<tr><td><strong>Olanzapine</strong></td><td>The best-evidenced medication in AN, though effect sizes are modest. RCTs show a small benefit for weight gain and reduction in obsessional eating-disorder cognition. Guidelines support its use as an adjunct, not a standalone treatment.</td><td>Weight gain (a clinical target here), sedation, metabolic effects. Cardiac monitoring required given QTc effects in a population already at cardiac risk. Generally used when other treatment is insufficient.</td></tr>
<tr><td><strong>Anxiolytics</strong><br>(benzodiazepines)</td><td>Short-term pre-meal use has some rationale given the extreme anxiety around eating. Not evidence-based as ongoing treatment. Risk of dependence significant in AN population.</td><td>Discuss specific use with prescriber. Not a primary or ongoing strategy.</td></tr>
<tr><td><strong>Zinc supplementation</strong></td><td>Zinc deficiency is common in AN and exacerbates depression, appetite suppression, and taste abnormalities. Supplementation during refeeding is reasonable and low-risk. Effect size is modest but the rationale is sound.</td><td>Safe and inexpensive. Part of micronutrient replacement protocol during refeeding. Not a standalone treatment.</td></tr>
<tr><td><strong>Nasogastric / enteral feeding</strong></td><td>Not medication, but medical intervention. Used in medical emergencies or when oral intake is insufficient for medical stabilisation. Not a permanent solution and psychologically complex — associated with loss of control and trauma if not managed carefully.</td><td>Requires specialised medical and nursing team. Decision about use involves weighing medical necessity against psychological impact and therapeutic alliance.</td></tr>
</tbody>
</table>
<p><strong>Treating comorbidities:</strong> Most people with AN have significant co-occurring anxiety disorders, depression, OCD, or PTSD. Treating these effectively — with appropriate medication and psychological intervention — is important and may improve AN treatment engagement. The distinction between symptoms that are primary eating-disorder features and symptoms that are independent comorbidities requires clinical judgement.</p>"""
            }
        ]
    },
    {
        "label": "Recovery and Psychology",
        "optional": True,
        "items": [
            {
                "id": "an_perfectionism_control",
                "title": "Perfectionism, control, and the function of restriction",
                "body": """<p><strong>Perfectionism in AN:</strong> Not all perfectionism is the same. In AN, the most clinically relevant form is <em>self-oriented perfectionism combined with self-criticism</em> — the internal demand for flawless performance in domains that matter, combined with harsh self-evaluation when standards are not met. Food and eating become a domain where perfect performance is achievable (or feels achievable): the rules are clear, compliance is measurable, and deviation is immediately punishable.</p>
<p><strong>Why perfectionism maintains AN:</strong></p>
<ul>
<li>It makes the rules of restriction feel necessary and virtuous, not disordered</li>
<li>Any deviation from the rules (eating more than planned, eating "forbidden" foods) triggers intense self-criticism that reinforces restriction as the corrective response</li>
<li>It generalises: AN perfectionism is usually not limited to eating — it appears in academic performance, relationships, appearance, and productivity</li>
<li>It creates cognitive inflexibility: rules are followed without flexibility, and exceptions are experienced as catastrophic failures rather than normal variations</li>
</ul>
<p><strong>Control and predictability:</strong> For many people with AN, restriction provides a sense of predictability and mastery at a time — or in a life — where other things feel uncontrollable. This is not simply a metaphor. The physiological effects of restriction (increased focus, emotional blunting, reduced appetite awareness after adaptation) provide concrete experiences of control that are genuinely reinforcing.</p>
<p><strong>What treatment does with this:</strong> Effective treatment does not simply remove the sense of control — it helps build alternative sources of mastery, competence, and predictability that do not depend on restriction. Values-based work (identifying what a full life without the eating disorder would look like and gradually moving toward it) is central to this. Treatment that strips away the function of AN without offering anything in its place reliably fails.</p>
<p><strong>The body as the last refuge of control:</strong> For some people, particularly those who have experienced trauma, abuse, or chronic feelings of helplessness, the body becomes the one domain where control feels possible. Understanding this — not pathologising it — is essential. The restriction is doing something. Recovery means finding other ways to do it.</p>"""
            },
            {
                "id": "body_image",
                "title": "Body image — disturbance, checking, and what actually helps",
                "body": """<p><strong>Body image disturbance is a diagnostic feature of AN</strong> — not a secondary symptom or a surface concern. It involves genuinely altered perception and processing of the body, not simply low self-esteem or social comparison. Understanding the nature of this disturbance informs why "just look in a mirror and see what's really there" is not a helpful intervention.</p>
<p><strong>Three components of body image disturbance:</strong></p>
<ul>
<li><strong>Perceptual disturbance:</strong> Genuinely inaccurate perception of body size and shape. Brain imaging studies confirm altered activity in regions processing body-related visual information. This is not consciously chosen distortion — it is a neurologically mediated perceptual difference, partly driven by malnutrition and partly by altered self-referential processing in AN.</li>
<li><strong>Cognitive disturbance:</strong> The over-evaluation of weight and shape as a measure of self-worth. In AN, how the body looks and how much it weighs carries a disproportionate weight in determining how the person evaluates themselves overall. One bad eating day can collapse global self-worth — a cognitive pattern that would be recognisably disproportionate in almost any other domain.</li>
<li><strong>Affective disturbance:</strong> Intense, often overwhelming negative emotion in response to body-related stimuli — feeling disgust, shame, anxiety, or despair in response to touching or looking at the body, wearing certain clothes, or encountering weight-related information.</li>
</ul>
<p><strong>Body checking and avoidance:</strong> Both maintain body image disturbance. Checking (repeated measurement, mirror scrutiny, feeling bones, comparing) provides temporary reassurance that drives the cycle. Avoidance (refusing to look, wearing loose clothing, avoiding scales) prevents the formation of accurate, stable perception. Neither resolves the disturbance — both entrench it.</p>
<p><strong>What actually helps:</strong></p>
<ul>
<li>Nutritional rehabilitation — significant improvement in body image occurs with weight restoration, suggesting a neurological component</li>
<li>Mirror exposure — structured, gradual, non-evaluative exposure to one's own body in a therapeutic context (not simply looking in the mirror, but learning to observe without judgment)</li>
<li>Reducing checking and avoidance behaviours systematically, with support</li>
<li>Cognitive work on the over-evaluation of shape and weight — rebuilding self-worth on multiple domains simultaneously</li>
<li>Mindfulness and body-based practices that develop interoceptive awareness rather than appearance-based evaluation</li>
</ul>"""
            },
            {
                "id": "an_relationships",
                "title": "AN and relationships — what the illness does to the people around you",
                "body": """<p><strong>AN is not a private condition.</strong> Its effects ripple through close relationships, family systems, and social networks. Understanding these effects — for the person with AN and for those close to them — is part of comprehensive care.</p>
<p><strong>What AN does to relationships:</strong></p>
<ul>
<li><strong>Social restriction:</strong> Eating is a social activity. Avoiding meals, refusing invitations, leaving early, bringing only specific foods, or becoming distressed around communal eating progressively narrows the social world. Isolation is both a consequence and a maintaining factor of AN.</li>
<li><strong>Secrecy:</strong> The ego-syntonic nature of AN — and the awareness that others will be concerned — drives concealment. Deception about eating, weight, and behaviour is common and is better understood as an illness feature than a character flaw. It does not mean the person does not care about honesty in other domains.</li>
<li><strong>Emotional unavailability:</strong> Malnutrition impairs emotional range and expressiveness. Partners and family members often describe the person as "not there" — present but not emotionally engaged. This is a consequence of the physiological state, not a relational choice.</li>
<li><strong>Role changes:</strong> Parents become food supervisors. Partners become carers. Siblings are often overlooked in the family distress. These role changes are real and require active management.</li>
</ul>
<p><strong>For families and partners:</strong></p>
<ul>
<li>Your response to the illness matters clinically. High levels of expressed emotion (criticism, hostility, overprotection) are associated with worse outcomes. Not because you cause the illness — but because the relational environment affects recovery.</li>
<li>Carer burden in AN is substantial and real. Your own mental health, including carer-specific support, matters both for you and for the person with AN.</li>
<li>Skills-based workshops for carers (the FREED model, New Maudsley approach, FEAST resources) provide concrete tools for supporting without accommodating the illness.</li>
</ul>
<p><strong>Intimacy and AN:</strong> Low body weight suppresses libido through hormonal pathways. Body image disturbance makes physical intimacy frightening or intolerable. AN often develops or worsens at developmental transitions involving intimacy. Recovery frequently requires specific work on the relationship between AN and sexuality and intimacy — work that is rarely offered but often needed.</p>"""
            },
            {
                "id": "an_recovery_identity",
                "title": "Recovery — what it involves and what it asks",
                "body": """<p><strong>Recovery from AN is not the same as finishing a course of treatment.</strong> It is a process — typically years long — that involves not just changes in eating and weight but fundamental shifts in identity, emotional regulation, relationships, and sense of self. Understanding what recovery actually involves prevents both premature closure ("I'm weight restored so I'm fine") and false hopelessness ("I'll never be free of this").</p>
<p><strong>What full recovery looks like:</strong></p>
<ul>
<li>Eating flexibly without distress — able to eat in social situations, with variety, without rules governing every decision</li>
<li>Weight maintained in a healthy range without ongoing, active effort to suppress it</li>
<li>Body image that allows normal function — not necessarily perfect contentment with appearance, but not preoccupied or impaired</li>
<li>Self-worth not primarily determined by weight, shape, or eating behaviour</li>
<li>Capacity to feel and manage emotions without using restriction as the primary regulation strategy</li>
<li>Social and relational life not restricted by the eating disorder</li>
</ul>
<p><strong>What recovery asks of the person:</strong></p>
<ul>
<li>Tolerating the profound anxiety and unfamiliarity of an eating pattern that does not follow ED rules</li>
<li>Giving up a sense of identity that has often been present for years</li>
<li>Developing alternative sources of competence, safety, and self-definition</li>
<li>Sitting with weight-restored body discomfort while the perceptual and cognitive disturbance catches up with physical change</li>
<li>Rebuilding relationships, ambitions, and a sense of future that AN has narrowed or eliminated</li>
</ul>
<p><strong>Relapse:</strong> Recovery from AN is rarely linear. Periods of improvement are often followed by periods of renewed restriction, particularly during stress, transitions, and losses. Relapse does not mean failure or that recovery is impossible — it is a predictable part of the course that requires a planned response rather than catastrophising. Early intervention when relapse begins is strongly associated with better outcomes than waiting until the situation deteriorates.</p>
<p><strong>The research on long-term outcomes:</strong> Long-term follow-up studies (10–20 years) consistently show better outcomes than the clinical pessimism around AN suggests. Approximately 50% achieve full recovery by that point. Recovery continues to occur decades into the illness. The illness is serious and the course is long — but it is not hopeless, and this must be communicated clearly.</p>"""
            }
        ]
    },
    {
        "label": "Products and Resources",
        "optional": True,
        "items": [
            {
                "id": "an_books",
                "title": "Recommended books",
                "body": """<p><strong>Brave Girl Eating</strong> — Harriet Brown. A parent's memoir of her daughter's AN and FBT treatment. One of the most honest and clinically informed accounts of AN and its treatment from a family perspective. Important reading for parents, and valuable for adults to understand what their families experience.</p>
<p><strong>Brave New Girl</strong> — Harriet Brown. Continuation of the above from the daughter's perspective as an adult. Both books together provide a rare dual account of the same recovery.</p>
<p><strong>Life Without Ed</strong> — Jenni Schaefer. Widely used in clinical settings. Schaefer externalises AN as "Ed" — a relationship to be ended. Some people find this framework transformative; others find it doesn't fit their experience. Worth encountering and deciding.</p>
<p><strong>8 Keys to Recovery from an Eating Disorder</strong> — Carolyn Costin &amp; Gwen Schubert Grabb. Written by a therapist who is also a recovered person with AN. Practical, compassionate, and evidence-informed. Covers the psychological, relational, and identity aspects of recovery well.</p>
<p><strong>Hunger: A Memoir of (My) Body</strong> — Roxane Gay. Not specifically about AN, but one of the most honest explorations of the relationship between trauma, body, and eating in contemporary literature. Clinically useful for understanding the body as a site of meaning-making.</p>
<p><strong>The Art of Starving</strong> — Sam J. Miller. A novel — not a self-help book. Provides a raw, non-romanticised portrait of AN in a male adolescent. Valuable for reducing the gendered framing of AN and for young men seeking recognition of their experience in literature.</p>
<p><strong>Professional reading:</strong> <em>Cognitive Behavior Therapy and Eating Disorders</em> — Christopher Fairburn. The clinical text underlying CBT-E. Detailed and evidence-based. For clinicians or particularly motivated patients wanting to understand the therapeutic model.</p>"""
            },
            {
                "id": "an_services_resources",
                "title": "Services, support, and resources",
                "body": """<p><strong>The Butterfly Foundation (Australia)</strong> — National eating disorder support organisation. Helpline (1800 33 4673), online chat, clinical referral directory, resources for carers and families. <a href="https://butterfly.org.au" target="_blank">butterfly.org.au</a></p>
<p><strong>Butterfly National Helpline — 1800 33 4673</strong> — Free, confidential support for people with eating disorders and their families. Counsellors are trained in eating disorders specifically. Available Monday to Friday.</p>
<p><strong>NEDC (National Eating Disorders Collaboration)</strong> — Australian clinical guidance, service directories, and professional and consumer resources. <a href="https://www.nedc.com.au" target="_blank">nedc.com.au</a></p>
<p><strong>InsideOut Institute</strong> — Australian clinical research and treatment centre for eating disorders at the University of Sydney. Clinical services, research participation, resources. <a href="https://insideout.org.au" target="_blank">insideout.org.au</a></p>
<p><strong>FEAST (Families Empowered and Supporting Treatment of Eating Disorders)</strong> — International peer support and education for parents and caregivers of people with eating disorders. Evidence-aligned, based on FBT principles. <a href="https://www.feast-ed.org" target="_blank">feast-ed.org</a></p>
<p><strong>Recovery Record</strong> — App designed for use alongside eating disorder treatment. Meal logging, mood tracking, coping skills, and direct messaging with clinicians (where integrated). Designed to reduce anxiety around meals and track progress between sessions. Evidence base is emerging. <a href="https://www.recoveryrecord.com" target="_blank">recoveryrecord.com</a></p>
<p><strong>NEDA (National Eating Disorders Association)</strong> — US-based, but has extensive evidence-based resources including screening tools, crisis text line, and treatment finder. <a href="https://www.nationaleatingdisorders.org" target="_blank">nationaleatingdisorders.org</a></p>
<p><strong>Lifeline — 13 11 14</strong> — 24/7 crisis support. The Butterfly Helpline is more specific to eating disorders, but Lifeline is available around the clock.</p>"""
            }
        ]
    }
]

def build_items_js(groups):
    lines = []
    lines.append("var AN_PE_GROUPS=[")
    for gi, g in enumerate(groups):
        label = "null" if g["label"] is None else ("'" + esc(g["label"]) + "'")
        optional = "true" if g["optional"] else "false"
        lines.append("  {label:" + label + ",optional:" + optional + ",items:[")
        for ii, item in enumerate(g["items"]):
            title = esc(item["title"])
            body = esc(item["body"])
            body = body.replace("\n", " ").replace("  ", " ")
            comma = "," if ii < len(g["items"]) - 1 else ""
            lines.append("    {id:'" + item["id"] + "',title:'" + title + "',body:'" + body + "'}" + comma)
        group_comma = "," if gi < len(groups) - 1 else ""
        lines.append("  ]}" + group_comma)
    lines.append("]")
    return "\n".join(lines)

groups_js = build_items_js(groups)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Anorexia Nervosa Psychoeducation — Dr Benjamin Murrie</title>
<style>
:root{--bg:#f0f2f5;--surface:#fff;--border:#e2e6ed;--text:#1a1d23;--muted:#6b7280;--an:#9d174d;--an-bg:#fdf2f8;--an-dark:#831843;--an-mid:#be185d;--navy:#0f172a;--sans:-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--text);font-size:15px;min-height:100vh}
.topbar{background:var(--navy);padding:10px 14px;border-bottom:3px solid var(--an);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.topbar-title{font-size:13px;font-weight:800;color:#fbcfe8;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ti{background:#1e293b;border:1px solid #334155;color:#f1f5f9;padding:5px 9px;border-radius:7px;font:inherit;font-size:13px;min-width:0}
.ti::placeholder{color:#64748b}
.ti:focus{outline:1px solid var(--an);background:#243349}
.content{max-width:1000px;margin:0 auto;padding:14px 12px 40px}
.condition-block{margin-bottom:14px;border-radius:10px;overflow:hidden;border:1px solid var(--border)}
.condition-header{padding:10px 14px;font:700 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:10px;background:var(--an-dark)}
.cond-sel-btns{margin-left:auto;display:flex;gap:5px;flex-shrink:0}
.cond-sel-btn{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);color:#fff;font:600 11px var(--sans);padding:3px 10px;border-radius:5px;cursor:pointer;transition:background .1s}
.cond-sel-btn:hover{background:rgba(255,255,255,.3)}
.topic-list{background:#fff}
.pe-group-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);padding:10px 14px 5px;background:#f8fafc;border-top:1px solid #f0f2f5}
.pe-section{border-top:1px solid #f4f5f8}
.pe-section:first-child{border-top:none}
.pe-header{display:flex;align-items:center;gap:9px;padding:9px 14px;cursor:pointer;user-select:none;-webkit-user-select:none}
.pe-header:hover{background:#f9fafb}
.pe-tick-btn{font-size:1rem;color:var(--muted);flex-shrink:0;min-width:20px;text-align:center;line-height:1;padding:2px;border-radius:4px;transition:color .1s}
.pe-title{font-weight:600;font-size:13px;color:var(--text);flex:1;line-height:1.35}
.pe-arrow{font-size:9px;color:var(--muted);flex-shrink:0;transition:transform .15s;margin-left:auto}
.pe-section.pe-open .pe-arrow{transform:rotate(90deg)}
.pe-body{display:none;padding:8px 14px 14px 43px;font-size:12.5px;line-height:1.65;color:#374151;border-top:1px solid #f4f5f8}
.pe-section.pe-open .pe-body{display:block}
.pe-body p{margin:0 0 7px}
.pe-body p:last-child{margin:0}
.pe-body ul{margin:4px 0 8px 16px}
.pe-body li{margin-bottom:4px}
.pe-body table{width:100%;border-collapse:collapse;font-size:11.5px;margin:6px 0 10px}
.pe-body th{background:#fdf2f8;padding:5px 8px;text-align:left;border:1px solid var(--border);font-size:11px}
.pe-body td{padding:4px 8px;border:1px solid var(--border);vertical-align:top}
.pe-body a{color:var(--an-mid)}
.pe-section.an-done{background:#fdf2f8}
.pe-section.an-done .pe-tick-btn{color:var(--an)}
.pe-section.pe-optional{opacity:.88}
.export-row{background:#fff;border:1px solid var(--border);border-radius:10px;padding:11px 14px;margin-bottom:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.export-row .ex-label{font:700 12px var(--sans);color:var(--muted);flex-shrink:0;white-space:nowrap}
.abtn{padding:7px 14px;border-radius:8px;border:1.5px solid var(--border);background:#fff;color:var(--text);font:600 12px var(--sans);cursor:pointer;transition:background .1s,border-color .1s}
.abtn:hover{background:#f3f4f6;border-color:#94a3b8}
.abtn.copied{background:#dcfce7;border-color:#86efac;color:#166534}
.preview-wrap{background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.preview-head{background:#f8fafc;border-bottom:1px solid var(--border);padding:9px 14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.preview-head-title{font:700 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.preview-body{padding:22px 26px;font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#111;min-height:100px}
.preview-body .empty-msg{color:var(--muted);font-style:italic;text-align:center;padding:36px 20px;font-size:11pt}
.ho-header{margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e5e7eb}
.ho-pt{font-size:17pt;font-weight:800;color:#0f172a;margin-bottom:2px}
.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:12px}
.ho-notice{font-size:9.5pt;background:#fdf2f8;border-left:3px solid #9d174d;padding:9px 12px;line-height:1.5;color:#831843}
.ho-group-label{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:14px 0 6px;padding-bottom:3px;border-bottom:2px solid currentColor}
.ho-group-label.an-g-core{color:#831843;border-bottom-color:#831843}
.ho-group-label.an-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.an-g-recovery{color:#0e7490;border-bottom-color:#0e7490}
.ho-group-label.an-g-resources{color:#065f46;border-bottom-color:#065f46}
.ho-topic{margin-bottom:7px;padding:9px 12px;border:1px solid #e5e7eb;border-radius:7px;background:#fffbfd}
.ho-topic-title{font-weight:700;font-size:11pt;color:#0f172a;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb}
.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151}
.ho-topic-body p{margin:0 0 6px}
.ho-topic-body p:last-child{margin:0}
.ho-topic-body ul{margin:3px 0 7px 16px}
.ho-topic-body li{margin-bottom:3px}
.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:5px 0 8px}
.ho-topic-body th{background:#fdf2f8;padding:4px 7px;text-align:left;border:1px solid #d1d5db;font-size:9pt}
.ho-topic-body td{padding:3pt 7pt;border:1px solid #d1d5db;vertical-align:top}
.ho-topic-body a{color:#9d174d}
.ho-footer{margin-top:24px;padding-top:12px;border-top:1px solid #e5e7eb;font-size:8.5pt;color:#9ca3af;font-style:italic}
</style>
</head>
<body>
<div class="topbar">
  <span class="topbar-title">Anorexia Nervosa Psychoeducation</span>
  <input class="ti" id="ptName" placeholder="Patient name..." style="flex:1;min-width:130px;max-width:210px" oninput="refresh()">
  <input class="ti" id="ptDate" type="date" style="flex:0 0 128px" oninput="refresh()">
  <input class="ti" id="drName" placeholder="Clinician name..." style="flex:1;min-width:130px;max-width:200px" oninput="refresh()">
</div>
<div class="content">
  <div class="condition-block" style="margin-top:12px">
    <div class="condition-header">
      Anorexia Nervosa — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll()">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll()">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="an-topic-list"></div>
  </div>
  <div class="export-row">
    <span class="ex-label">Export</span>
    <button class="abtn" id="btn-docx" onclick="dlDocx()">Download .docx</button>
    <button class="abtn" id="btn-plain" onclick="copyPlain(this)">Copy plain text</button>
    <button class="abtn" id="btn-fmt" onclick="copyFormatted(this)">Copy formatted</button>
  </div>
  <div class="preview-wrap">
    <div class="preview-head">
      <span class="preview-head-title">Handout Preview</span>
      <button class="abtn" onclick="refresh()" style="padding:4px 11px;font-size:11px">Refresh</button>
    </div>
    <div class="preview-body" id="preview">
      <div class="empty-msg">Tick topics above to generate the handout.</div>
    </div>
  </div>
</div>
<script>
var sel={};
function $(id){return document.getElementById(id);}
function f(id){var el=$(id);return el?el.value.trim():\'\';}
function esc(s){if(!s)return \'\';return String(s).replace(/&/g,\'&amp;\').replace(/</g,\'&lt;\').replace(/>/g,\'&gt;\').replace(/"/g,\'&quot;\');}

''' + groups_js + r'''

function renderTopics(){
  var el=$('an-topic-list'); if(!el) return;
  var html='';
  AN_PE_GROUPS.forEach(function(g){
    if(g.label) html+='<div class="pe-group-label">'+(g.optional?'<span style="font-size:9px;opacity:.6;font-weight:600;margin-right:4px">OPTIONAL</span>':'')+esc(g.label)+'</div>';
    g.items.forEach(function(item){
      var done=!!sel[item.id];
      html+='<div class="pe-section'+(done?' an-done':'')+(g.optional?' pe-optional':'')+'" data-id="'+item.id+'">';
      html+='<div class="pe-header"><span class="pe-tick-btn">'+(done?'&#9745;':'&#9744;')+'</span>';
      html+='<span class="pe-title">'+esc(item.title)+'</span>';
      html+='<span class="pe-arrow">&#9658;</span></div>';
      html+='<div class="pe-body">'+item.body+'</div></div>';
    });
  });
  el.innerHTML=html;
  el.addEventListener('click',function(e){
    var sec=e.target.closest('[data-id]'); if(!sec) return;
    var id=sec.getAttribute('data-id');
    if(e.target.classList.contains('pe-tick-btn')){
      e.stopPropagation();
      sel[id]=!sel[id];
      sec.classList.toggle('an-done',!!sel[id]);
      sec.querySelector('.pe-tick-btn').innerHTML=sel[id]?'&#9745;':'&#9744;';
      refresh();
    } else {
      var hdr=e.target.closest('.pe-header'); if(hdr) sec.classList.toggle('pe-open');
    }
  });
}
function selectAll(){AN_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){sel[item.id]=true;});});renderTopics();refresh();}
function clearAll(){Object.keys(sel).forEach(function(k){sel[k]=false;});renderTopics();refresh();}
var GROUP_COLOR_CLASS={'null':'an-g-core','Treatment':'an-g-treatment','Recovery and Psychology':'an-g-recovery','Products and Resources':'an-g-resources'};
function buildHandout(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var hasAny=false;
  AN_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){if(sel[item.id])hasAny=true;});});
  if(!hasAny) return null;
  var h='<div class="ho-header">';
  h+='<div class="ho-pt">Anorexia Nervosa — Psychoeducation Handout</div>';
  h+='<div class="ho-meta">Patient: <strong>'+esc(name)+'</strong>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <strong>'+esc(dr)+'</strong></div>';
  h+='<div class="ho-notice">The following information was discussed or provided as educational material during your appointment. It is a reference guide only — all treatment decisions should be made in consultation with your treating clinician.</div></div>';
  AN_PE_GROUPS.forEach(function(g){
    var gItems=g.items.filter(function(item){return sel[item.id];});
    if(!gItems.length) return;
    var gKey=g.label||'null';
    var cls=GROUP_COLOR_CLASS[gKey]||'an-g-core';
    if(g.label) h+='<div class="ho-group-label '+cls+'">'+esc(g.label)+'</div>';
    gItems.forEach(function(item){
      h+='<div class="ho-topic"><div class="ho-topic-title">'+esc(item.title)+'</div>';
      h+='<div class="ho-topic-body">'+item.body+'</div></div>';
    });
  });
  h+='<div class="ho-footer">This handout was prepared specifically for '+esc(name)+(ds?' following a psychiatric appointment on '+esc(ds):'')+'. It is not a substitute for clinical advice.</div>';
  return h;
}
function refresh(){
  var html=buildHandout();
  var pv=$('preview');
  if(!html){pv.innerHTML='<div class="empty-msg">Tick topics above to generate the handout.</div>';return;}
  pv.innerHTML=html;
}
function buildDocxHtml(){
  var html=buildHandout(); if(!html) return null;
  return '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">'+
    '<head><meta charset="UTF-8"><style>'+
    '@page{margin:2cm 2.5cm;}body{font-family:Arial,sans-serif;font-size:11pt;line-height:1.5;color:#111;}'+
    '.ho-header{margin-bottom:14pt;padding-bottom:10pt;border-bottom:1pt solid #e5e7eb;}'+
    '.ho-pt{font-size:17pt;font-weight:bold;color:#0f172a;margin-bottom:3pt;}'+
    '.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:10pt;}'+
    '.ho-notice{font-size:9.5pt;background:#fdf2f8;border-left:3pt solid #9d174d;padding:8pt 10pt;color:#831843;}'+
    '.ho-group-label{font-size:8.5pt;font-weight:bold;text-transform:uppercase;letter-spacing:.06em;margin:12pt 0 5pt;padding-bottom:2pt;border-bottom:1.5pt solid currentColor;}'+
    '.ho-group-label.an-g-core{color:#831843;}.ho-group-label.an-g-treatment{color:#1e3a5f;}.ho-group-label.an-g-recovery{color:#0e7490;}.ho-group-label.an-g-resources{color:#065f46;}'+
    '.ho-topic{margin-bottom:7pt;padding:8pt 11pt;border:1pt solid #e5e7eb;background:#fffbfd;}'+
    '.ho-topic-title{font-weight:bold;font-size:11pt;color:#0f172a;margin:0 0 5pt;padding-bottom:4pt;border-bottom:1pt solid #e5e7eb;}'+
    '.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151;}'+
    '.ho-topic-body p{margin:0 0 5pt;}.ho-topic-body ul{margin:3pt 0 6pt 14pt;}.ho-topic-body li{margin-bottom:3pt;}'+
    '.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9pt;margin:5pt 0 8pt;}'+
    '.ho-topic-body th{background:#fdf2f8;padding:4pt 6pt;text-align:left;border:1pt solid #d1d5db;font-size:8.5pt;}'+
    '.ho-topic-body td{padding:3pt 6pt;border:1pt solid #d1d5db;vertical-align:top;}'+
    '.ho-footer{margin-top:20pt;padding-top:10pt;border-top:1pt solid #e5e7eb;font-size:8pt;color:#9ca3af;font-style:italic;}'+
    '</style></head><body>'+html+'</body></html>';
}
function dlDocx(){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected.');return;}
  var name=(f('ptName')||'Patient').replace(/[^a-zA-Z0-9]/g,'_');
  var blob=new Blob(['﻿'+docx],{type:'application/msword;charset=utf-8'});
  var url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='AN_Handout_'+name+'.doc';
  document.body.appendChild(a);a.click();document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);},2000);
  flash($('btn-docx'),'Downloaded!');
}
function copyPlain(btn){
  if(!buildHandout()){alert('No topics selected.');return;}
  navigator.clipboard.writeText($('preview').innerText||'').then(function(){flash(btn,'Copied!');}).catch(function(){});
}
function copyFormatted(btn){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected.');return;}
  if(window.ClipboardItem){
    var blob=new Blob([docx],{type:'text/html'});
    navigator.clipboard.write([new ClipboardItem({'text/html':blob})]).then(function(){flash(btn,'Copied!');}).catch(function(){
      navigator.clipboard.writeText($('preview').innerText||'').then(function(){flash(btn,'Copied (plain)!');});
    });
  } else {
    navigator.clipboard.writeText($('preview').innerText||'').then(function(){flash(btn,'Copied!');});
  }
}
function flash(btn,msg){
  if(!btn)return;
  var orig=btn.textContent;btn.textContent=msg;btn.classList.add('copied');
  setTimeout(function(){btn.textContent=orig;btn.classList.remove('copied');},2000);
}
document.addEventListener('DOMContentLoaded',function(){
  var td=new Date().toISOString().slice(0,10);
  var dtEl=$('ptDate'); if(dtEl&&!dtEl.value) dtEl.value=td;
  renderTopics();
  refresh();
});
</script>
</body>
</html>'''

with open('/home/user/psychiatric-tools/an-psychoeducation.html', 'w', encoding='utf-8') as fh:
    fh.write(html)
print("Done.")
