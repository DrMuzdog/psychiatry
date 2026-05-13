#!/usr/bin/env python3
"""Generate bp1-psychoeducation.html — Bipolar 1 Disorder psychoeducation tool."""

def esc(s):
    return s.replace("'", "\\'")

groups = [
    {
        "label": None,
        "optional": False,
        "items": [
            {
                "id": "what_bp1",
                "title": "What is Bipolar 1 Disorder?",
                "body": """<p><strong>Definition:</strong> Bipolar 1 Disorder (BD1) is characterised by at least one manic episode. Unlike Bipolar 2 (which requires a hypomanic but not full manic episode), Bipolar 1 is defined by the presence of mania — which is categorically more severe than hypomania, often requires hospitalisation, and can include psychotic features. Depressive episodes occur in the vast majority of people with BD1 but are not required for the diagnosis.</p>
<p><strong>The spectrum of bipolar disorders:</strong></p>
<ul>
<li><strong>Bipolar 1:</strong> At least one full manic episode (≥7 days, or any duration if hospitalisation required or psychotic features present)</li>
<li><strong>Bipolar 2:</strong> Hypomanic episodes only (not full mania) plus at least one depressive episode</li>
<li><strong>Cyclothymia:</strong> Chronic instability with hypomanic and depressive symptoms not meeting full episode criteria</li>
<li><strong>Unspecified bipolar:</strong> Clinically significant bipolar features not fitting the above categories</li>
</ul>
<p><strong>Prevalence and onset:</strong> BD1 affects approximately 1% of the population worldwide — roughly the same as schizophrenia. Mean age of onset is late teens to mid-20s. It affects men and women roughly equally, though men more commonly present first with mania and women more often present first with depression. BD1 is one of the most heritable psychiatric conditions — heritability estimates are 80–90%, comparable to height.</p>
<p><strong>Diagnosis is frequently delayed:</strong> The average delay from first symptoms to correct diagnosis is 5–10 years. This occurs because: the first episode is often depressive (and treated as major depression); mania may not be recognised as pathological by the person experiencing it; and symptoms can be attributed to personality, substance use, or situational factors. Delayed diagnosis means delayed appropriate treatment — which matters because episodes cause neurobiological harm.</p>
<p><strong>What it is not:</strong></p>
<ul>
<li>Mood swings or being "a bit up and down" — BD1 episodes are distinct, sustained, and often severe</li>
<li>Caused by trauma, bad parenting, or character weakness — it is a neurobiological condition with strong genetic loading</li>
<li>A reason to not achieve a full, meaningful life — many people with BD1 manage it well with appropriate treatment</li>
</ul>"""
            },
            {
                "id": "mania",
                "title": "Mania — what it is, and why it feels so good",
                "body": """<p><strong>DSM-5 criteria for a manic episode:</strong> A distinct period of abnormally and persistently elevated, expansive, or irritable mood AND abnormally and persistently increased goal-directed activity or energy, lasting at least 7 days (or any duration if hospitalisation is required). During the same period, at least 3 of the following symptoms (4 if mood is only irritable) must be present to a significant degree:</p>
<p><strong>DIGFAST — the manic symptom mnemonic:</strong></p>
<ul>
<li><strong>D</strong>istractibility — attention easily drawn to irrelevant stimuli</li>
<li><strong>I</strong>mpulsivity / indiscretion — reckless financial decisions, sexual behaviour, substance use, business ventures</li>
<li><strong>G</strong>randiosity — inflated self-esteem, sense of special purpose, may become delusional ("I am chosen"; "I have discovered the solution to climate change")</li>
<li><strong>F</strong>light of ideas — thoughts racing, tangential, difficult to follow</li>
<li><strong>A</strong>ctivity — increased goal-directed activity (often many projects simultaneously, none completed)</li>
<li><strong>S</strong>leep — decreased need for sleep (not insomnia — the person does not feel tired after 2–3 hours)</li>
<li><strong>T</strong>alkative — pressured speech, difficult to interrupt, talks over others</li>
</ul>
<p><strong>The paradox — mania often feels wonderful:</strong> This is the central clinical challenge of mania. Euphoric mania feels like enhanced clarity, creativity, confidence, productivity, and freedom from normal constraints. People in manic episodes often describe feeling "like the best version of myself" or "finally alive." This is not an exaggeration — elevated mood, boundless energy, reduced sleep without fatigue, and grandiosity genuinely feel like assets rather than symptoms. The implication: people frequently do not seek help, resist treatment, and may look back on manic episodes with nostalgia even after they have caused significant harm.</p>
<p><strong>Severe mania and psychosis:</strong> Approximately 50–75% of manic episodes involve psychotic features. These are typically mood-congruent: grandiose delusions (special mission, superhuman abilities), auditory hallucinations (voices affirming greatness or giving instructions). Severe mania can be indistinguishable from primary psychotic disorders — correct diagnosis requires longitudinal history.</p>
<p><strong>Mixed features:</strong> Manic episodes with concurrent significant depressive symptoms (dysphoria, suicidal ideation, hopelessness) alongside the energy and impulsivity of mania. This is arguably the most dangerous state in psychiatry — the person has the psychomotor activation to act on suicidal thoughts. Requires urgent clinical attention.</p>
<p><strong>Consequences of untreated mania:</strong> Financial devastation from impulsive spending or investment; relationship breakdown from sexual indiscretion or behavioural changes; legal consequences; loss of employment; accommodation loss; harm from risk-taking behaviour. The person who "feels fine" during mania typically faces these consequences when the episode resolves.</p>"""
            },
            {
                "id": "bp1_depression",
                "title": "Bipolar depression — the other half, and the greater risk",
                "body": """<p><strong>Depression predominates over a lifetime:</strong> In prospective studies, people with BD1 spend significantly more time in depressive than manic phases — approximately 3:1 in terms of episode time. Despite this, treatment research has historically focused more on mania. Bipolar depression is the phase that most impairs quality of life and carries the greatest mortality risk.</p>
<p><strong>How bipolar depression differs from unipolar depression:</strong></p>
<ul>
<li><strong>Hypersomnia</strong> more common than insomnia (though both occur)</li>
<li><strong>Hyperphagia</strong> more common than appetite loss (though both occur)</li>
<li><strong>Psychomotor retardation</strong> — "leaden paralysis," profound slowing</li>
<li><strong>Mixed features</strong> in up to 40% — concurrent manic symptoms (racing thoughts, irritability, agitation, decreased sleep) alongside depressive mood and anhedonia</li>
<li><strong>Atypical features</strong> more common — mood reactivity, rejection sensitivity, increased sleep, increased appetite</li>
<li><strong>Psychotic features</strong> possible (typically mood-congruent — nihilistic, guilt-laden)</li>
</ul>
<p><strong>Suicide — the primary cause of premature death in BD1:</strong> Bipolar disorder carries a lifetime suicide attempt rate of approximately 25–50% and a completed suicide rate 15–20 times the general population. This exceeds the suicide risk in major depressive disorder alone. The risk is highest during depressive and mixed episodes. Every depressive episode in BD1 requires explicit suicidality assessment. Lithium has a specific, independent anti-suicidal effect that is one of the strongest arguments for its use.</p>
<p><strong>Why antidepressants are problematic in BD1:</strong> Standard antidepressants (SSRIs, SNRIs, TCAs, bupropion) can precipitate manic switches, induce mixed states, and increase cycling frequency in BD1. This is why the standard treatment approach for bipolar depression differs fundamentally from unipolar depression. Antidepressants are not first-line; when used, they require mood stabiliser cover; and some — particularly bupropion and venlafaxine — carry higher switching risk than others. Many RANZCP and international guidelines recommend against antidepressant monotherapy in BD1 entirely.</p>
<p><strong>Seek help early for depressive episodes:</strong> The window for early intervention is narrow — early treatment of a depressive episode is associated with shorter episode duration and reduced risk of progression to mixed states. If you notice early warning signs of depression (see Triggers section), contact your psychiatrist rather than waiting to see if it resolves.</p>"""
            },
            {
                "id": "bp1_neuroscience",
                "title": "The neuroscience of Bipolar 1",
                "body": """<p><strong>This is a brain condition, not a personality trait.</strong> Neuroimaging, genetics, and biochemistry consistently demonstrate that BD1 involves measurable, reproducible changes in brain structure and function. Understanding these changes clarifies why medication is not optional and why lifestyle factors matter.</p>
<p><strong>The kindling hypothesis:</strong> Each manic or depressive episode lowers the neurobiological threshold for the next. Early in the illness, episodes are often precipitated by clear external stressors. Over time, episodes become increasingly autonomous — the brain requires less provocation to enter a pathological state. This means that episode prevention is not simply about avoiding suffering in the moment — it is about protecting future brain function. Every prevented episode is neurobiologically protective.</p>
<p><strong>Circadian rhythm dysregulation:</strong> The circadian timing system — the internal clock governing sleep, cortisol, body temperature, and dozens of other physiological rhythms — is fundamentally dysregulated in BD1. The suprachiasmatic nucleus (the brain's master clock) shows abnormal function in BD1 independent of current episode status. This is the neurobiological basis for why sleep disruption is both a trigger for and an early warning sign of episodes, and why Interpersonal and Social Rhythm Therapy (IPSRT) — which directly targets circadian regularity — is an evidence-based psychological treatment.</p>
<p><strong>Dopamine and glutamate:</strong> Mania is associated with hyperdopaminergic activity — dopamine excess drives the reward, grandiosity, impulsivity, and hyperactivity. Antipsychotics work by reducing dopamine receptor stimulation. The glutamate system (NMDA/AMPA) is also dysregulated, contributing to both depressive and manic neurochemistry. Lithium and anticonvulsant mood stabilisers modulate glutamate transmission.</p>
<p><strong>HPA axis dysregulation:</strong> Cortisol hypersecretion is present in depressive phases and contributes to hippocampal damage. Stress sensitisation — where the HPA axis becomes increasingly reactive over the illness course — is analogous to kindling.</p>
<p><strong>Neuroprogression — why episodes matter beyond suffering:</strong> Neuroimaging studies demonstrate progressive structural brain changes with multiple untreated episodes: hippocampal volume loss, prefrontal cortical thinning, white matter changes. These correlate with cognitive impairment. This neuroprogression is not inevitable — it is substantially attenuated by sustained mood stabiliser treatment, particularly lithium, which has direct neuroprotective properties (promotes BDNF, inhibits GSK-3β, reduces apoptosis). The argument for long-term medication in BD1 is in part a neuroprotective argument.</p>"""
            },
            {
                "id": "bp1_triggers_ews",
                "title": "Triggers and early warning signs",
                "body": """<p><strong>Why early warning signs matter:</strong> Most people with BD1 can identify a period of 2–7 days between the first warning signs of an episode and full syndrome emergence. Early intervention during this prodromal window — contacting your psychiatrist, adjusting sleep, reducing stimulation — is far more effective than waiting until the episode is fully established.</p>
<p><strong>Sleep — the single most important signal:</strong> Reduced sleep with NOT feeling tired is the most reliable early warning sign of impending mania. For many people, even one or two nights of reduced sleep can be both a trigger and a prodrome simultaneously. The relationship is bidirectional: sleep disruption triggers episodes, and early episodes disrupt sleep. <strong>Rule: if you find you are sleeping less than usual and do not feel tired — contact your psychiatrist that day, not next week.</strong></p>
<p><strong>Common manic triggers:</strong></p>
<ul>
<li>Sleep disruption (travel across time zones, new baby, shift work, late nights)</li>
<li>Positive as well as adverse stress — promotions, exciting new projects, new relationships, major life changes</li>
<li>Spring — many people with BD1 have a seasonal pattern with spring mania and winter/autumn depression</li>
<li>Stimulant substances — caffeine, cocaine, amphetamines, MDMA; even cannabis can trigger mania in some</li>
<li>Stopping or reducing mood stabiliser medication</li>
<li>Antidepressants (see Bipolar Depression section)</li>
<li>Postpartum period — the highest-risk period for mania/psychosis in women with BD1; requires specific medication planning</li>
</ul>
<p><strong>Common depressive triggers:</strong></p>
<ul>
<li>Autumn/winter for those with seasonal pattern</li>
<li>Life losses and psychosocial stressors</li>
<li>Sleep disruption (can trigger depression as well as mania)</li>
<li>Alcohol — directly depressogenic; also impairs medication adherence</li>
<li>Social isolation and interpersonal conflict</li>
</ul>
<p><strong>Developing your personal relapse signature:</strong> Early warning signs are partly universal (sleep, energy, irritability) and partly individual. With your treatment team, document specifically what the first 3–5 days of an approaching manic episode and depressive episode look like for you — not in general terms ("I feel more energetic") but specific observable behaviours (e.g., "I start new projects late at night," "I stop reading, which I usually enjoy," "I become irritable with my partner"). A written relapse plan should include: what to watch for; who to contact; what to do first; and emergency contacts.</p>"""
            }
        ]
    },
    {
        "label": "Treatment",
        "optional": False,
        "items": [
            {
                "id": "bp1_tx_overview",
                "title": "Treatment — why lifelong medication is standard",
                "body": """<p><strong>The central principle:</strong> Bipolar 1 Disorder requires ongoing treatment, not episodic treatment. This is not because the person cannot manage without medication some of the time — many can — but because the neurobiological evidence shows that repeated episodes are harmful, that medication substantially reduces episode frequency and severity, and that the risks of untreated BD1 (suicide, neuroprogression, social and occupational harm) substantially exceed the risks of properly managed pharmacotherapy.</p>
<p><strong>Three treatment goals:</strong></p>
<ul>
<li><strong>Acute episode treatment:</strong> Resolve mania, mixed states, or depressive episodes rapidly and safely</li>
<li><strong>Maintenance (prophylaxis):</strong> Prevent future episodes — this is where the most benefit accumulates over time</li>
<li><strong>Inter-episode wellbeing:</strong> Address residual symptoms, cognitive function, quality of life, and comorbidities between episodes</li>
</ul>
<p><strong>Combination treatment is the norm:</strong> Most people with BD1 require a combination of a mood stabiliser (lithium, valproate, or lamotrigine) and an atypical antipsychotic for optimal management. Monotherapy is sometimes achievable in mild presentations but is the exception rather than the rule in BD1.</p>
<p><strong>Psychoeducation is itself a treatment:</strong> The Barcelona group (Colom, Vieta et al) demonstrated in RCTs that structured group psychoeducation programmes significantly reduce episode frequency and hospitalisation rates compared to standard care. The information in this handout is not supplementary to treatment — it is part of it. Knowing your illness, its neurobiology, your warning signs, and your treatment options directly improves outcomes.</p>
<p><strong>Medical comorbidity:</strong> BD1 is associated with significantly elevated rates of metabolic syndrome, cardiovascular disease, and type 2 diabetes — partly from medication effects and partly from the illness itself. This means regular physical health monitoring (metabolic panel, weight, lipids, glucose) is a non-optional component of care. Many people with BD1 die prematurely from cardiovascular disease — this is preventable with appropriate monitoring and management.</p>
<p><strong>RANZCP guidelines (Australia):</strong> The Royal Australian and New Zealand College of Psychiatrists Clinical Practice Guidelines for Mood Disorders (2015, updated) are the reference standard for BD management in Australia. These are publicly available and inform the evidence-based recommendations in this handout.</p>"""
            },
            {
                "id": "bp1_acute_mania",
                "title": "Managing acute mania — what happens and what helps",
                "body": """<p><strong>Recognition:</strong> Acute mania often requires others to initiate help — the person experiencing mania frequently lacks insight that anything is wrong. Partners, family, and friends often recognise the episode before the person with BD1 does. This is neurobiological, not wilful denial — the brain state of mania impairs self-assessment.</p>
<p><strong>When hospitalisation is necessary:</strong></p>
<ul>
<li>Safety concerns — impaired judgment putting the person or others at risk</li>
<li>Psychotic features</li>
<li>Severe agitation or inability to care for self</li>
<li>Medication initiation requiring close monitoring (lithium loading, high-dose antipsychotics)</li>
<li>Failure of community management</li>
<li>Insufficient social support for safe community management</li>
</ul>
<p><strong>Involuntary admission:</strong> When mania impairs insight completely and the person refuses hospitalisation, Mental Health Act provisions exist in all Australian states and territories for involuntary admission. This is a protective mechanism, not a punishment. Discussing advance care directives and Ulysses agreements (a pre-written instruction that the person gives permission for certain interventions when unwell) while well is strongly recommended.</p>
<p><strong>Pharmacological management of acute mania:</strong></p>
<ul>
<li><strong>First-line:</strong> Atypical antipsychotics (olanzapine, quetiapine, aripiprazole, risperidone) — fast-acting, effective for both psychotic and non-psychotic mania</li>
<li><strong>Benzodiazepines:</strong> Lorazepam or diazepam for acute agitation — as adjunct, not primary treatment</li>
<li><strong>Valproate:</strong> Can be loaded rapidly (20mg/kg/day) — useful for faster mania control</li>
<li><strong>Lithium:</strong> Effective for mania but takes 7–10 days; not suitable as sole acute agent; always combine with antipsychotic acutely</li>
<li><strong>Stop precipitants:</strong> Cease antidepressants, reduce stimulant substances, optimise sleep environment</li>
</ul>
<p><strong>Prioritise sleep:</strong> In the prodrome and early episode, restoring sleep is a therapeutic intervention in its own right. Benzodiazepines, quetiapine, and olanzapine all have sedating properties that can help establish sleep. Even a single night of adequate sleep can slow early manic escalation.</p>
<p><strong>After the episode:</strong> Post-manic depression is extremely common — the "crash" after mania can be severe and carries high suicide risk. Close monitoring is essential in the weeks following mania resolution.</p>"""
            },
            {
                "id": "bp1_depression_tx",
                "title": "Treating bipolar depression — different rules from unipolar",
                "body": """<p><strong>The core difference:</strong> Bipolar depression cannot be treated the same way as unipolar depression. Antidepressants as monotherapy are contraindicated; the first-line agents are fundamentally different; and the risks of triggering mania must always be considered alongside the risks of undertreated depression.</p>
<p><strong>First-line pharmacological options for bipolar depression in Australia:</strong></p>
<ul>
<li><strong>Quetiapine:</strong> PBS-listed for bipolar depression; strong evidence from BOLDER I/II trials; 50–300mg nocte; both full and low doses effective; sedating — helpful for sleep disruption</li>
<li><strong>Lithium:</strong> Evidence for acute bipolar depression and anti-suicidal effect; takes several weeks; best for those not yet on lithium or with inadequate levels</li>
<li><strong>Lamotrigine:</strong> Best evidence for preventing depressive recurrence (not acute treatment); slow titration required; see Medications section</li>
<li><strong>Lurasidone:</strong> PBS-listed in Australia for bipolar depression; PREVAIL I/II trial evidence; metabolically neutral; requires food (see Medications section)</li>
<li><strong>Olanzapine-fluoxetine combination:</strong> Evidence from BD depression trials; weight gain from olanzapine is a practical limitation</li>
</ul>
<p><strong>Antidepressants — the controversy:</strong> International guidelines vary on antidepressant use in BD1 depression. The most conservative (and increasingly evidence-supported) position is to avoid antidepressants entirely in BD1, using quetiapine, lurasidone, or lithium instead. If antidepressants are used, they must be paired with a mood stabiliser, SSRIs are preferred over SNRIs/bupropion/TCAs, and the prescriber and patient must agree in advance on what to do if switching or activation occurs.</p>
<p><strong>ECT (Electroconvulsive Therapy):</strong> Highly effective for both severe bipolar depression and acute mania. Carries strong evidence including in pregnancy when pharmacotherapy is limited. Significantly underutilised. Should be considered earlier in BD1 depression than in unipolar depression, particularly with psychotic features, severe suicidality, or medication failure.</p>
<p><strong>Ketamine / esketamine:</strong> Emerging evidence for rapid antidepressant effect in bipolar depression. Not without mania-switch risk. Currently used in specialist settings. Nasal esketamine (Spravato) is TGA-approved for treatment-resistant depression in Australia but not specifically BD.</p>"""
            },
            {
                "id": "bp1_psychology",
                "title": "Psychological therapies for Bipolar 1",
                "body": """<p><strong>Psychological treatment in BD1 is adjunctive — it does not replace medication, but it substantially improves outcomes when added to pharmacotherapy.</strong></p>
<p><strong>Cognitive Behavioural Therapy for Bipolar (CBT-BD):</strong> Modified CBT specifically designed for BD. Components include: recognition of prodromal symptoms and implementation of response plans; activity scheduling during depressive phases; cognitive restructuring of grandiose and depressive cognitions; relapse prevention; medication adherence work; addressing unhelpful beliefs about the illness (e.g., "I need my mania to be creative"). Differs from standard depression CBT in the explicit inclusion of mania management and the bipolar relapse cycle.</p>
<p><strong>Interpersonal and Social Rhythm Therapy (IPSRT):</strong> Designed specifically for BD — the only major psychotherapy developed exclusively for this population. Combines standard interpersonal therapy (addressing grief, role transitions, conflicts) with Social Rhythm Therapy: tracking and regularising the timing of social rhythms (sleep, wake, meals, activity, social contact) to stabilise circadian rhythms. Strong evidence from RCTs showing reduced episode frequency, longer time to relapse, and improved functioning. The Social Rhythm Metric (SRM) diary is a concrete tool used in IPSRT that can be adapted for self-monitoring.</p>
<p><strong>Family-Focused Therapy (FFT):</strong> Involves the patient and key family members or partner. Three phases: psychoeducation about BD for the whole family; communication enhancement training; problem-solving skills. Specifically reduces "expressed emotion" (criticism, emotional over-involvement, and hostility in the family environment) which is a strong predictor of relapse in BD. RCT evidence for reduced relapse and hospitalisation. Particularly important in adolescent-onset BD1.</p>
<p><strong>Psychoeducation groups:</strong> The Barcelona model (Colom, Vieta et al) — 21-session structured group for people with BD1 or BD2. Covers illness understanding, treatment rationale, early warning signs, lifestyle regularity, substances, and coping. RCT evidence for significantly reduced episodes and hospitalisation over 5-year follow-up. Available at some Australian tertiary centres.</p>
<p><strong>What is NOT recommended as primary treatment:</strong> Unstructured supportive therapy without BD-specific components; psychodynamic therapy alone; standard mindfulness-based programmes not adapted for BD (risk of triggering mania in some). Some people find mindfulness helpful for depressive phases specifically — discuss with your psychiatrist before starting.</p>"""
            }
        ]
    },
    {
        "label": "Medications",
        "optional": False,
        "items": [
            {
                "id": "med_lithium",
                "title": "Lithium — gold standard mood stabiliser | PBS listed",
                "body": """<p><strong>Class:</strong> Mood stabiliser (elemental salt). <strong>TGA/PBS status:</strong> Listed for mania and maintenance treatment of bipolar disorder. <strong>Brands in Australia:</strong> Lithicarb (lithium carbonate tablets); Priadel (lithium carbonate controlled-release); Quilonum SR (lithium carbonate SR). <strong>In use since:</strong> 1949 — the oldest and most evidence-based mood stabiliser.</p>
<p><strong>Mechanism:</strong> Multiple: inhibits glycogen synthase kinase-3β (GSK-3β — reducing dopamine signalling and having neuroprotective effects); inositol depletion hypothesis (reduces phosphatidylinositol second-messenger signalling in hyperactive circuits); BDNF upregulation (neuroprotective); circadian clock gene modulation; reduces apoptosis in neurons. The breadth of its neurobiological effects is unique and probably why its clinical profile is difficult to match with any single-target agent.</p>
<p><strong>Evidence — why lithium remains essential:</strong></p>
<ul>
<li>Superior to placebo and most alternatives for <strong>prevention of both manic and depressive recurrence</strong></li>
<li>The only medication with <strong>specific anti-suicidal effect</strong> independent of mood stabilisation — Cipriani meta-analysis (2013): significant reduction in all-cause mortality and suicide in long-term lithium users</li>
<li><strong>Neuroprotective</strong>: associated with increased hippocampal volume, reduced cortical atrophy, attenuated neuroprogression</li>
<li>Possibly reduces dementia risk with long-term use</li>
</ul>
<p><strong>Therapeutic levels (serum lithium, trough — 12 hours after last dose):</strong></p>
<table>
<tr><th>Indication</th><th>Target level (mmol/L)</th><th>Notes</th></tr>
<tr><td>Acute mania</td><td>0.8–1.2</td><td>Higher end of range; monitor closely</td></tr>
<tr><td>Maintenance (standard)</td><td>0.6–0.8</td><td>Most patients maintained here; balances efficacy and tolerability</td></tr>
<tr><td>Elderly / renally impaired</td><td>0.4–0.6</td><td>Lower target to reduce toxicity risk</td></tr>
<tr><td>Toxicity risk</td><td>&gt;1.5</td><td>Mild toxicity; &gt;2.0 = serious; &gt;2.5 = potentially fatal</td></tr>
</table>
<p><strong>Dosing:</strong> Typically 600–1800mg/day in divided doses or SR formulation once daily at night. Start 400–600mg/day, increase based on levels. Check first level 5–7 days after starting or dose change; then at 2 weeks; monthly for 3 months; then 3-monthly when stable.</p>
<p><strong>Monitoring schedule:</strong></p>
<table>
<tr><th>Test</th><th>Frequency</th><th>Why</th></tr>
<tr><td>Serum lithium (trough)</td><td>Every 3 months when stable; after any dose change</td><td>Narrow therapeutic index</td></tr>
<tr><td>eGFR / creatinine / UEC</td><td>Every 6 months</td><td>Long-term nephrotoxicity; lithium is renally cleared</td></tr>
<tr><td>TSH</td><td>Every 6–12 months</td><td>Hypothyroidism occurs in ~30% long-term; treat with thyroxine, do not stop lithium</td></tr>
<tr><td>Calcium</td><td>Annually</td><td>Hyperparathyroidism (rare but occurs)</td></tr>
<tr><td>ECG</td><td>Baseline; if cardiac symptoms</td><td>T-wave changes common, not usually clinically significant</td></tr>
</table>
<p><strong>Drug interactions — critical:</strong></p>
<table>
<tr><th>Drug</th><th>Effect on lithium</th><th>Clinical action</th></tr>
<tr><td>NSAIDs (ibuprofen, naproxen, diclofenac)</td><td>Increase levels by 25–60%</td><td>Avoid; use paracetamol instead</td></tr>
<tr><td>ACE inhibitors / ARBs</td><td>Increase levels significantly</td><td>Reduce lithium dose; monitor closely</td></tr>
<tr><td>Thiazide diuretics</td><td>Increase levels significantly</td><td>Avoid; loop diuretics (frusemide) safer</td></tr>
<tr><td>Metronidazole, some antibiotics</td><td>Can increase levels</td><td>Monitor levels during course</td></tr>
<tr><td>Caffeine</td><td>Reduces levels (increases renal clearance)</td><td>Consistent caffeine intake; avoid sudden changes</td></tr>
</table>
<p><strong>Dehydration and toxicity risk:</strong> Lithium excretion mirrors sodium excretion. Dehydration (illness, vomiting, diarrhoea, hot weather, excessive sweating, reduced fluid intake) causes lithium retention and can rapidly produce toxicity. <strong>Sick day rules:</strong> If unwell with significant vomiting, diarrhoea, or reduced oral intake — hold lithium, ensure hydration, check level if unwell &gt;24h. Inform prescriber.</p>
<p><strong>Toxicity signs — act immediately:</strong> Nausea, vomiting, diarrhoea (these first); then coarse tremor, ataxia, dysarthria, confusion, drowsiness. These are emergencies — stop lithium, seek medical care, and check level urgently. Severe toxicity (level &gt;2.5) can cause permanent neurological damage or death.</p>
<p><strong>Common side effects (not toxicity):</strong> Fine resting tremor (often responds to dose reduction or propranolol); polyuria and polydipsia (nephrogenic partial DI — consider amiloride if troublesome); weight gain; cognitive blunting/"brain fog" at higher levels; hypothyroidism (~30%, treat with thyroxine); acne or psoriasis exacerbation; GI upset (take with food, use SR formulation).</p>
<p><strong>Pregnancy:</strong> Lithium crosses the placenta. Ebstein's anomaly risk (tricuspid valve malformation) was historically overestimated; current data suggests absolute risk approximately 1:1000 (vs 1:20,000 baseline) — elevated but not prohibitive. Risk-benefit discussion is essential. Dose adjustment is needed (renal clearance increases in pregnancy; then falls acutely postpartum — hold dose at delivery). Postpartum period is highest-risk time; continue lithium postpartum even with breastfeeding (low transfer to breast milk).</p>
<p><strong>Long-term renal effects:</strong> Chronic lithium use causes tubular dysfunction in most patients and clinically significant eGFR reduction in approximately 20–30% over decades. This requires monitoring but rarely mandates cessation — the risk of stopping lithium (relapse, suicide) often outweighs renal risk for most patients. Discuss with nephrologist if eGFR &lt;45.</p>"""
            },
            {
                "id": "med_valproate",
                "title": "Sodium valproate — effective but teratogenic | PBS listed",
                "body": """<p><strong>Class:</strong> Anticonvulsant / mood stabiliser. <strong>PBS status:</strong> Listed for mania and epilepsy. <strong>Brands in Australia:</strong> Epilim (sodium valproate); Epilim Chrono / Valpro CR (extended-release); Depakote (valproate semisodium — available in AU, somewhat different formulation).</p>
<p><strong>Mechanism:</strong> Enhances GABA activity (inhibits GABA transaminase, increases GABA synthesis); blocks voltage-gated sodium channels; inhibits histone deacetylase (epigenetic effects, neuroprotective); modulates dopaminergic and serotonergic systems.</p>
<p><strong>Evidence:</strong> Effective for acute mania (equivalent to lithium in many trials) and maintenance. May have advantages over lithium for: mixed states; rapid cycling; secondary mania (due to general medical conditions or substance use); and patients who cannot tolerate lithium. Not as strongly evidence-based as lithium for suicide prevention.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Phase</th><th>Dose</th><th>Notes</th></tr>
<tr><td>Starting dose</td><td>200–500mg BD or nocte</td><td>With food; start lower in elderly/small patients</td></tr>
<tr><td>Acute mania loading</td><td>20mg/kg/day in divided doses</td><td>Faster mania control; monitor level and side effects</td></tr>
<tr><td>Maintenance range</td><td>1000–2500mg/day</td><td>Divided doses or extended-release once-daily nocte</td></tr>
<tr><td>Therapeutic level</td><td>350–700 μmol/L (50–100 mg/L)</td><td>Check 12h post-dose (trough)</td></tr>
</table>
<p><strong>Monitoring:</strong> LFTs and FBC at baseline, 6 weeks, then 6-monthly; weight at every review; serum level when clinically indicated (adherence, efficacy, toxicity concern); platelet count if bleeding symptoms.</p>
<p><strong>⚠️ TERATOGENICITY — major safety issue, mandatory discussion for any patient with childbearing potential:</strong></p>
<p>Sodium valproate is one of the most teratogenic medications in clinical use. Risks include:</p>
<ul>
<li><strong>Neural tube defects (spina bifida):</strong> 1–2% (vs 0.06% baseline) — dose-dependent</li>
<li><strong>Cardiac malformations:</strong> ~2-fold increased risk</li>
<li><strong>Neurodevelopmental effects:</strong> IQ reduction of 7–10 points on average; autism spectrum traits in 5–10% of exposed children; ADHD features; language delays. These effects may persist into adulthood.</li>
<li><strong>Risk is dose-dependent:</strong> Higher doses carry substantially greater risk</li>
</ul>
<p><strong>Australian Valproate Pregnancy Prevention Programme (VPPP):</strong> In 2024, the TGA mandated the Australian Valproate Pregnancy Prevention Programme. Requirements include: documented discussion of teratogenicity risk; confirmation of effective contraception use for all patients with childbearing potential; annual review; and specific patient acknowledgement forms. Prescribers are legally required to follow this programme. Valproate should <strong>not</strong> be prescribed to patients with childbearing potential who are not using highly effective contraception, unless no alternatives exist and the patient has fully understood the risks.</p>
<p><strong>Side effects:</strong> Weight gain (significant, often 5–10kg; dose-dependent); sedation (particularly at higher doses); nausea and GI upset (use extended-release and take with food); tremor; hair loss (zinc and selenium supplementation may help); thrombocytopenia (check platelets if bruising); elevated transaminases (usually transient and benign at &lt;3× ULN; stop if &gt;3× ULN); pancreatitis (rare but serious — stop if persistent upper abdominal pain); hyperammonaemia (rare, causes encephalopathy — check ammonia if confusion develops on valproate).</p>
<p><strong>Drug interactions:</strong></p>
<ul>
<li><strong>Lamotrigine:</strong> Valproate doubles lamotrigine serum levels — halve lamotrigine dose when combining (see Lamotrigine section); this combination is clinically useful but requires careful dose adjustment</li>
<li><strong>Carbamazepine:</strong> Reduces valproate levels; carbamazepine levels also affected</li>
<li><strong>Aspirin:</strong> Displaces valproate from protein binding, increasing free drug levels; avoid high-dose aspirin</li>
<li><strong>Meropenem and other carbapenems:</strong> Dramatically and rapidly reduce valproate levels — do not use together if possible</li>
</ul>"""
            },
            {
                "id": "med_lamotrigine",
                "title": "Lamotrigine — for depression prevention | slow titration essential",
                "body": """<p><strong>Class:</strong> Anticonvulsant / mood stabiliser. <strong>PBS status:</strong> Listed for epilepsy in Australia; widely used off-label for BD (common practice, recognised in RANZCP guidelines). <strong>Brands:</strong> Lamictal (branded); generic lamotrigine widely available.</p>
<p><strong>Critical framing:</strong> Lamotrigine is <strong>not</strong> effective for acute mania and <strong>should not be used as the sole agent</strong> in BD1 without an antimanic medication (lithium, valproate, or antipsychotic) to cover the manic pole. Its primary evidence base is <strong>prevention of bipolar depressive episodes</strong>. In BD1, it should almost always be used in combination with a primary mood stabiliser that covers mania.</p>
<p><strong>Mechanism:</strong> Blocks voltage-gated sodium channels and stabilises neuronal membranes; reduces glutamate release; weak calcium channel effects. Unlike valproate, minimal GABA effects. The antidepressant mechanism is not fully understood but appears to involve glutamate modulation and downstream synaptic plasticity.</p>
<p><strong>Evidence:</strong> Calabrese et al (2000) and subsequent maintenance trials: lamotrigine significantly delays time to depressive recurrence in BD. Less effective for mania prevention. The combination of lamotrigine + lithium provides coverage of both poles and is a common maintenance strategy.</p>
<p><strong>⚠️ Titration — MUST be slow; rushing causes serious rash:</strong></p>
<table>
<tr><th>Weeks</th><th>Standard dose</th><th>With valproate (halve dose)</th><th>With carbamazepine (double dose)</th></tr>
<tr><td>1–2</td><td>25mg daily</td><td>12.5mg daily (or 25mg every other day)</td><td>50mg daily</td></tr>
<tr><td>3–4</td><td>50mg daily</td><td>25mg daily</td><td>100mg daily</td></tr>
<tr><td>5–6</td><td>100mg daily</td><td>50mg daily</td><td>200mg daily</td></tr>
<tr><td>7+</td><td>200mg daily (target)</td><td>100mg daily</td><td>300–400mg daily</td></tr>
<tr><td>Maximum</td><td>400mg/day</td><td>200mg/day with valproate</td><td>400–600mg/day</td></tr>
</table>
<p><strong>⚠️ Stevens-Johnson Syndrome (SJS) / Toxic Epidermal Necrolysis (TEN):</strong></p>
<p>SJS/TEN is a rare (0.1–0.3%) but potentially life-threatening mucocutaneous reaction. Risk is greatest in the first 8 weeks and is substantially reduced by slow titration. Counsel ALL patients specifically before starting lamotrigine:</p>
<ul>
<li>Any new rash while on lamotrigine = <strong>stop lamotrigine and seek medical review that day</strong></li>
<li>Rash + flu-like symptoms (fever, sore throat, mouth ulcers, eye redness) = <strong>medical emergency; present to ED</strong></li>
<li>Minor rashes are common (~10%) and not always SJS — but the patient cannot distinguish them; all rashes require prompt review</li>
<li>Do NOT restart lamotrigine after stopping for a rash without specialist advice — rechallenge risk is high</li>
</ul>
<p><strong>Common side effects (not SJS):</strong> Headache (often settles); nausea; dizziness; diplopia at higher doses; ataxia at higher doses; insomnia (take in the morning or midday if this occurs).</p>
<p><strong>Advantages:</strong> Weight neutral (often preferred over valproate and olanzapine for this reason); relatively favourable cognitive profile; no significant metabolic effects; reasonable safety in pregnancy (cleft palate risk exists but lower than valproate; folic acid supplementation important).</p>
<p><strong>Drug interactions:</strong> Valproate doubles lamotrigine levels (see Valproate section — halve lamotrigine dose). Carbamazepine halves lamotrigine levels (need higher lamotrigine doses). Oral contraceptives reduce lamotrigine levels by ~50% — levels drop on starting OCP and rise when pill stopped (risk of toxicity on OCP cessation — adjust doses).</p>"""
            },
            {
                "id": "med_quetiapine",
                "title": "Quetiapine — mania, depression, and maintenance | PBS listed",
                "body": """<p><strong>Class:</strong> Atypical antipsychotic. <strong>PBS status:</strong> Listed in Australia for acute mania, bipolar depression (important — this is separate from its listing for schizophrenia), and maintenance in BD. <strong>Brands:</strong> Seroquel (IR and XR); generic quetiapine widely available.</p>
<p><strong>Mechanism:</strong> D2 receptor antagonism (lower affinity than typical antipsychotics); 5-HT2A antagonism (contributing to antidepressant effect); H1 antagonism (sedation); α1 and α2 antagonism; 5-HT1A partial agonism. The norquetiapine metabolite inhibits noradrenaline reuptake, contributing to antidepressant properties. The combination of receptor actions makes quetiapine one of the few agents with evidence for both poles of BD.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Indication</th><th>Starting dose</th><th>Target dose</th><th>Formulation</th></tr>
<tr><td>Acute mania</td><td>100mg nocte or BD</td><td>400–800mg/day</td><td>IR or XR</td></tr>
<tr><td>Bipolar depression</td><td>50mg nocte</td><td>50–300mg nocte</td><td>IR or XR; lower doses effective</td></tr>
<tr><td>Maintenance</td><td>As for acute episode</td><td>300–600mg/day</td><td>XR preferred for adherence</td></tr>
</table>
<p><strong>Important — bipolar depression dosing:</strong> The BOLDER I/II and EMBOLDEN trials used 300mg and 600mg. However, clinical experience and some data suggest lower doses (50–150mg) may be effective for bipolar depression with fewer metabolic side effects — particularly for patients who need some anxiolytic/sleep benefit without heavy sedation. Titrate to the dose that provides clinical effect.</p>
<p><strong>Side effects:</strong></p>
<ul>
<li><strong>Sedation:</strong> Most prominent at lower doses (paradoxically); H1 antagonism; useful for insomnia but impairs function if excessive. Dose at night. Tolerance develops over weeks.</li>
<li><strong>Weight gain:</strong> Significant — average 2–4kg; more with higher doses and younger patients. Monitor BMI and waist circumference.</li>
<li><strong>Metabolic syndrome:</strong> Hyperlipidaemia, hyperglycaemia, diabetes risk. Monitor fasting glucose and lipids.</li>
<li><strong>Orthostatic hypotension:</strong> Particularly on initiation; α1 blockade; rise slowly, adequate hydration.</li>
<li><strong>QTc prolongation:</strong> Modest but dose-related; check ECG at higher doses and in patients with cardiac risk factors.</li>
<li><strong>Dry mouth, constipation, urinary retention:</strong> Anticholinergic effects.</li>
<li><strong>Tardive dyskinesia:</strong> With long-term use, lower risk than typical antipsychotics but not zero; review annually.</li>
</ul>
<p><strong>Metabolic monitoring (RANZCP / Australian guidelines):</strong> Weight, waist circumference, blood pressure, fasting glucose, fasting lipids at baseline; at 1 month; at 3 months; then 6-monthly. Refer to GP or endocrinologist if metabolic parameters deteriorate significantly.</p>
<p><strong>Drug interactions:</strong> CYP3A4 metabolism — inducers (carbamazepine, rifampicin) reduce levels significantly; inhibitors (fluconazole, erythromycin) increase levels. Additive QTc prolongation with other QTc-prolonging agents. Additive sedation with CNS depressants.</p>"""
            },
            {
                "id": "med_olanzapine",
                "title": "Olanzapine — highly effective for mania | metabolic monitoring essential",
                "body": """<p><strong>Class:</strong> Atypical antipsychotic. <strong>PBS status:</strong> Listed for acute mania and bipolar maintenance in Australia. <strong>Brands:</strong> Zyprexa; generic olanzapine widely available; Zyprexa Zydis (orodispersible); Zyprexa IntraMuscular (for acute agitation).</p>
<p><strong>Mechanism:</strong> Broad receptor antagonism including D2, D4, 5-HT2A/2C, H1, M1, α1. The high H1 and M1 affinity accounts for significant sedation, weight gain, and anticholinergic effects. Among the most potent D2 antagonists in clinical use, explaining both its antimanic efficacy and metabolic burden.</p>
<p><strong>Evidence:</strong> Olanzapine is one of the most effective antimanic agents available — among the highest response rates in head-to-head trials. The olanzapine-fluoxetine combination (OFC) has the strongest evidence base for acute bipolar depression among antipsychotic combinations.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Indication</th><th>Dose range</th><th>Notes</th></tr>
<tr><td>Acute mania</td><td>10–20mg/day (oral)</td><td>Can start 10mg nocte, increase to 20mg if needed</td></tr>
<tr><td>Acute agitation (IM)</td><td>5–10mg IM</td><td>Short-acting IM; max 3 doses in 24h; do not combine with IM lorazepam (respiratory risk)</td></tr>
<tr><td>Bipolar depression</td><td>5–20mg/day</td><td>Often in combination with fluoxetine 20–50mg</td></tr>
<tr><td>Maintenance</td><td>5–20mg/day</td><td>Use lowest effective dose; 5–10mg if primarily for maintenance</td></tr>
</table>
<p><strong>Metabolic side effects — the main limitation:</strong></p>
<ul>
<li><strong>Weight gain:</strong> Significant and often substantial — average 4–6kg in first year; can be 10–20kg with longer use; one of the most weight-promoting psychiatric medications available</li>
<li><strong>Diabetes:</strong> Risk of new-onset type 2 diabetes; monitor fasting glucose</li>
<li><strong>Dyslipidaemia:</strong> Elevated triglycerides particularly; monitor lipids</li>
<li><strong>Metabolic syndrome:</strong> The combination of weight gain, dyslipidaemia, and hyperglycaemia increases cardiovascular risk substantially</li>
</ul>
<p><strong>Metabolic monitoring (mandatory):</strong> Baseline: weight, BMI, waist circumference, blood pressure, fasting glucose, HbA1c, fasting lipids. Repeat at 1 month, 3 months, 6 months, then 6-monthly. Escalate metabolic intervention early — olanzapine-associated metabolic syndrome is not inevitable if addressed.</p>
<p><strong>Other side effects:</strong> Sedation (marked, typically at initiation; useful acutely but can persist); dry mouth; constipation; urinary retention; orthostatic hypotension; mild QTc prolongation.</p>
<p><strong>Practical advice:</strong> Olanzapine is often appropriate when rapid, reliable mania control is the priority — it works quickly and effectively. For long-term maintenance, metabolic burden must be weighed against efficacy. Metformin (500–1000mg/day) has evidence for attenuating olanzapine-associated weight gain and should be considered early if significant weight gain occurs.</p>"""
            },
            {
                "id": "med_aripiprazole",
                "title": "Aripiprazole — mania and maintenance | PBS listed | monthly injection available",
                "body": """<p><strong>Class:</strong> Partial dopamine agonist / atypical antipsychotic. <strong>PBS status:</strong> Listed for acute mania and bipolar maintenance in Australia. <strong>Brands:</strong> Abilify (oral tablets, orodispersible, oral solution, IM short-acting); Abilify Maintena (extended-release suspension, IM monthly — PBS listed for bipolar maintenance); generic aripiprazole oral widely available.</p>
<p><strong>Mechanism:</strong> Partial agonist at D2 and D3 receptors (the key distinguishing feature — functional antagonism in hyperdopaminergic states, functional agonism in hypodopaminergic states); partial agonist at 5-HT1A; antagonist at 5-HT2A; relatively low H1 and M1 affinity (explaining favourable metabolic and sedation profile).</p>
<p><strong>Evidence:</strong> RCT evidence for acute mania; long-term maintenance trials showing relapse prevention. Less evidence than lithium or valproate for depressive prevention — primarily used for the manic/hypomanic pole and maintenance. Not effective for bipolar depression as monotherapy.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Formulation</th><th>Starting dose</th><th>Target dose</th><th>Notes</th></tr>
<tr><td>Oral tablet</td><td>10–15mg daily</td><td>15–30mg daily</td><td>Morning dosing preferred (activating)</td></tr>
<tr><td>IM monthly (Maintena)</td><td>400mg IM gluteal</td><td>400mg monthly (can reduce to 300mg)</td><td>Must overlap with oral for first 2 weeks; PBS listed for maintenance</td></tr>
</table>
<p><strong>Advantages over olanzapine and quetiapine:</strong></p>
<ul>
<li>Weight neutral or minimal weight gain — significant advantage for long-term use</li>
<li>Metabolically favourable — minimal effect on glucose or lipids</li>
<li>No significant QTc prolongation</li>
<li>Monthly injection option for adherence (Abilify Maintena) — a major advantage in BD1 where medication adherence during wellness is a persistent challenge</li>
</ul>
<p><strong>Key side effect — akathisia:</strong> Subjective restlessness and inability to stay still — a prominent and often distressing side effect of aripiprazole in 10–20% of patients. Can be confused with agitation or anxiety. Dose-dependent. Management: dose reduction; propranolol 20–40mg BD; benztropine (less effective for akathisia than for EPS).</p>
<p><strong>Other side effects:</strong> Nausea (particularly on initiation — take with food); insomnia/activation (dose in morning; can worsen sleep if taken at night); headache; tremor; mild anxiety. Less sedation than quetiapine or olanzapine — advantageous for daytime function but may be insufficient for acute mania where sedation is therapeutically useful.</p>
<p><strong>Drug interactions:</strong> CYP2D6 and CYP3A4 substrate. CYP2D6 inhibitors (fluoxetine, paroxetine) increase levels by ~80% — reduce aripiprazole dose. Carbamazepine reduces levels ~70% — increase aripiprazole dose. Quinidine, ketoconazole also affect levels.</p>"""
            },
            {
                "id": "med_lurasidone",
                "title": "Lurasidone — bipolar depression | PBS listed in Australia | must take with food",
                "body": """<p><strong>Class:</strong> Atypical antipsychotic. <strong>PBS status:</strong> Listed in Australia specifically for bipolar depression (not just mania or schizophrenia) — an important distinction making it directly prescribable for this indication. <strong>Brand:</strong> Latuda.</p>
<p><strong>Mechanism:</strong> D2 antagonist; 5-HT2A antagonist; 5-HT7 antagonist (believed important for antidepressant properties — 5-HT7 blockade modulates circadian rhythm and glutamate/dopamine crosstalk); 5-HT1A partial agonist; α2C antagonist. Minimal H1, M1, or α1 activity — explaining the metabolically neutral and low-sedation profile.</p>
<p><strong>Evidence for bipolar depression:</strong> PREVAIL 1 (monotherapy) and PREVAIL 2 (adjunctive to lithium/valproate) trials: lurasidone 20–120mg/day significantly reduced MADRS depression scores versus placebo in BD depression. Both the 20–60mg and 80–120mg dose ranges showed efficacy. Effect size comparable to quetiapine and superior to many other options for bipolar depression specifically.</p>
<p><strong>⚠️ Must be taken with food — critical for efficacy:</strong> Lurasidone requires at least 350 calories of food to achieve adequate bioavailability. Without food, absorption drops by approximately 50%. This is not just a tolerability issue — it is an efficacy issue. Instruct patients specifically: take with your evening meal, not just a snack.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Phase</th><th>Dose</th><th>Notes</th></tr>
<tr><td>Starting dose</td><td>20mg nocte with evening meal</td><td>Low starting dose reduces nausea and akathisia on initiation</td></tr>
<tr><td>Usual therapeutic range</td><td>20–80mg nocte</td><td>PREVAIL trials showed good response across 20–80mg range</td></tr>
<tr><td>Maximum dose</td><td>160mg/day</td><td>Schizophrenia doses; BD evidence primarily up to 120mg</td></tr>
</table>
<p><strong>Advantages:</strong></p>
<ul>
<li>Metabolically neutral — minimal weight gain; no clinically significant effect on glucose or lipids; no QTc prolongation</li>
<li>PBS-listed specifically for bipolar depression in Australia — directly prescribable</li>
<li>Once-daily evening dosing with meal</li>
<li>Low EPS burden at therapeutic doses</li>
</ul>
<p><strong>Side effects:</strong> Nausea (most common — take with food, usually resolves within 2 weeks); akathisia (dose-related, 5–10%); somnolence; headache; dizziness.</p>
<p><strong>Drug interactions — important:</strong></p>
<ul>
<li><strong>Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir):</strong> Contraindicated — massively increase lurasidone levels</li>
<li><strong>Strong CYP3A4 inducers (carbamazepine, rifampicin, St John's Wort):</strong> Contraindicated — dramatically reduce lurasidone levels to sub-therapeutic</li>
<li><strong>Moderate CYP3A4 inhibitors (diltiazem, verapamil, erythromycin):</strong> Halve lurasidone dose</li>
<li><strong>Grapefruit juice:</strong> Inhibits CYP3A4 — avoid consistently</li>
</ul>
<p><strong>Australian prescribing note:</strong> As of 2024, lurasidone (Latuda) is PBS-listed in Australia for the treatment of bipolar I depression in adults. This makes it directly accessible at PBS cost without requiring off-label justification — a significant advance for treating the depressive pole of BD1.</p>"""
            },
            {
                "id": "med_carbamazepine",
                "title": "Carbamazepine — third-line mania | drug interactions and HLA testing",
                "body": """<p><strong>Class:</strong> Anticonvulsant / mood stabiliser. <strong>PBS status:</strong> Listed for epilepsy; off-label but widely used for mania/BD maintenance. <strong>Brands:</strong> Tegretol (immediate-release and CR); generic carbamazepine.</p>
<p><strong>Mechanism:</strong> Blocks voltage-gated sodium channels; reduces neuronal excitability; modulates dopamine and noradrenaline systems; weak calcium channel effects. Mechanism overlaps with valproate but through different primary pathways.</p>
<p><strong>Place in therapy:</strong> Third-line for mania in most guidelines — used when lithium and valproate are ineffective or not tolerated. Has evidence for acute mania and maintenance but less than lithium or valproate. May be particularly useful for mixed states, rapid cycling, or when valproate is contraindicated (women of childbearing potential).</p>
<p><strong>Dosing:</strong> 400–1600mg/day in 2–4 divided doses. Start 100–200mg BD, increasing by 200mg every 3–7 days. Therapeutic level: 17–50 μmol/L (4–12 mg/L) at trough.</p>
<p><strong>⚠️ HLA-B*1502 testing — mandatory before starting in patients of Asian ancestry (TGA recommendation):</strong> The HLA-B*1502 allele is associated with a dramatically increased risk of Stevens-Johnson syndrome and toxic epidermal necrolysis with carbamazepine exposure. This allele is prevalent in Han Chinese (5–10%), Southeast Asian, South Asian, and some other Asian populations but is rare (&lt;0.1%) in European-ancestry populations. The TGA recommends genetic testing for HLA-B*1502 before starting carbamazepine in patients of Asian ancestry. If positive — do not use carbamazepine.</p>
<p><strong>Drug interactions — carbamazepine is a potent CYP3A4, CYP2C9, and CYP2C19 inducer:</strong> It accelerates metabolism of many co-administered drugs, often reducing their levels to sub-therapeutic. Clinically important:</p>
<table>
<tr><th>Drug affected</th><th>Effect</th><th>Clinical consequence</th></tr>
<tr><td>Oral contraceptives</td><td>Levels reduced ~50%</td><td>Contraceptive failure — use non-hormonal or barrier method</td></tr>
<tr><td>Warfarin</td><td>Levels reduced</td><td>INR falls; increase warfarin dose; monitor closely</td></tr>
<tr><td>Quetiapine, aripiprazole, haloperidol</td><td>Levels reduced 60–75%</td><td>May need much higher antipsychotic doses</td></tr>
<tr><td>Lamotrigine</td><td>Levels reduced ~50%</td><td>Need approximately double the lamotrigine dose</td></tr>
<tr><td>Valproate</td><td>Mutual interaction</td><td>Both levels may be affected; monitor both</td></tr>
<tr><td>Many antibiotics, antifungals, antiretrovirals</td><td>Variable</td><td>Check interactions for each new medication</td></tr>
</table>
<p>Also an autoinducer — carbamazepine induces its own metabolism (autoinduction), meaning levels fall over the first 4–6 weeks even on a stable dose; re-check level at 4–6 weeks after starting or dose adjustment.</p>
<p><strong>Monitoring:</strong> FBC and LFTs at baseline, 2 weeks, monthly × 3, then 6-monthly (leucopenia, thrombocytopenia, hepatotoxicity possible); serum level; UEC (hyponatraemia due to SIADH in up to 10% — particularly elderly); body weight.</p>
<p><strong>Side effects:</strong> Dizziness and ataxia (dose-related — worse early in treatment and with rapid increases); diplopia; nausea; drowsiness; hyponatraemia (SIADH); lupus-like syndrome (rare); aplastic anaemia and agranulocytosis (rare but serious — persistent fever/infection warrants FBC check); SJS/TEN (higher risk in HLA-B*1502 carriers); cardiac conduction effects (generally only clinically relevant in pre-existing conduction disease).</p>
<p><strong>Teratogenicity:</strong> Neural tube defect risk approximately 1%; also associated with craniofacial defects. Folic acid supplementation important. Discuss with specialist if pregnancy planning.</p>"""
            }
        ]
    },
    {
        "label": "Living Well with Bipolar 1",
        "optional": True,
        "items": [
            {
                "id": "bp1_sleep",
                "title": "Sleep and circadian rhythm — the keystone of stability",
                "body": """<p><strong>Why sleep is the single most important lifestyle factor in BD1:</strong> Sleep is not just a correlate of mood state — it is a bidirectional driver. Disrupted sleep triggers episodes; episodes disrupt sleep. The circadian timing system is fundamentally dysregulated in BD1, making patients more vulnerable to sleep disruption as a trigger than the general population. Protecting sleep is protecting mood stability.</p>
<p><strong>The relationship is specific:</strong></p>
<ul>
<li>Reduced sleep with NOT feeling tired = possible impending mania — act immediately</li>
<li>Hypersomnia (sleeping too much) = possible impending or current depression</li>
<li>Sleep fragmentation and difficulty falling asleep = common in all phases; often a residual interepisode symptom requiring specific management</li>
</ul>
<p><strong>Social Rhythm Therapy — regularising the biological clock:</strong> IPSRT uses the Social Rhythm Metric: tracking the daily timing of 5 key activities — wake time, first contact with another person, start of work/school/housework, dinner, and bedtime. The goal is not rigid scheduling but regularity — the same activities at approximately the same times each day. Irregular timing of these activities is a stronger predictor of BD episodes than many clinical variables. The SRM can be adapted as a simple self-monitoring tool even outside formal IPSRT.</p>
<p><strong>Practical sleep rules for BD1:</strong></p>
<ul>
<li><strong>Consistent wake time is more important than consistent bedtime</strong> — the wake signal anchors the entire circadian rhythm; prioritise it above all else</li>
<li>Avoid sleeping in after disrupted nights — maintaining wake time prevents circadian drift</li>
<li>Limit naps to &lt;20 minutes before 3pm if needed; long or late naps fragment night sleep</li>
<li>Protect the bedroom for sleep — no phones, no screens in bed</li>
<li>Morning bright light (10,000 lux light box, 20–30 minutes after waking) — advances the circadian rhythm; particularly helpful in those with delayed sleep phase; also has direct mood-lifting effects in depressive phases</li>
</ul>
<p><strong>High-risk periods requiring specific sleep protection:</strong></p>
<ul>
<li><strong>Transmeridian travel (jet lag):</strong> High risk for mania. Strategies: melatonin, adjust light exposure, communicate travel plans to psychiatrist in advance</li>
<li><strong>New baby:</strong> Among the highest-risk periods for BD1 relapse due to sleep disruption; requires a specific perinatal management plan with your psychiatrist before birth</li>
<li><strong>Shift work:</strong> Ongoing circadian disruption; incompatible with good BD management if possible to avoid; if unavoidable, discuss specific risk management with your psychiatrist</li>
<li><strong>Exam periods, project deadlines:</strong> Sleep deprivation is a trigger; plan ahead to protect sleep even under study/work pressure</li>
</ul>
<p><strong>When sleep problems persist despite good sleep hygiene:</strong> CBT for Insomnia (CBT-I) has the strongest long-term evidence for insomnia and is safe in BD. Digital CBT-I programmes (Sleepio, SHUTi) are accessible. Avoid benzodiazepines and Z-drugs (zopiclone, zolpidem) for chronic insomnia — dependence risk and rebound effects. Short-term use in the context of prodromal mania is appropriate and different.</p>"""
            },
            {
                "id": "bp1_substances",
                "title": "Substances and Bipolar 1 — higher stakes than for most people",
                "body": """<p><strong>Substance use is more dangerous in BD1 than in the general population</strong> — for several reasons: substances directly trigger mood episodes; they impair medication adherence; they worsen the course of the illness over time; and comorbid substance use disorders occur at very high rates in BD1 (approximately 40–60% lifetime prevalence).</p>
<p><strong>Cannabis:</strong></p>
<ul>
<li>Significantly worsens the course of BD1 — associated with increased episode frequency, more hospitalisations, greater severity, poorer functional outcomes</li>
<li>THC specifically (not CBD) is the primary problem — cannabinoid 1 receptor stimulation in the mesolimbic system drives dopamine release and can directly precipitate manic episodes in vulnerable individuals</li>
<li>High-potency cannabis (most of what is now available) carries higher risk than lower-potency products historically used</li>
<li>Many people with BD1 use cannabis to manage sleep or anxiety — the perceived short-term benefit comes at significant long-term cost</li>
<li>The recommendation is clear: do not use cannabis in BD1</li>
</ul>
<p><strong>Alcohol:</strong></p>
<ul>
<li>Directly depressogenic — even moderate use worsens bipolar depressive episodes and inter-episode mood</li>
<li>Disrupts sleep (see Sleep section) — the same sleep disruption that can trigger mania</li>
<li>Impairs medication adherence — people are less likely to take medications reliably when drinking regularly</li>
<li>Interacts with several BD medications (lithium levels affected by dehydration; valproate CNS depression additive; sedative effects of quetiapine/olanzapine additive)</li>
<li>Low-risk guidelines (NHMRC 2020): ≤4 standard drinks on any day, ≤10/week. For BD1, lower is better — this is a situation where "no alcohol" is genuinely a reasonable choice, not an overcaution</li>
</ul>
<p><strong>Stimulants (cocaine, methamphetamine, MDMA, prescription stimulants misused):</strong></p>
<ul>
<li>Can directly precipitate manic episodes — hyperdopaminergic states that the BD1 brain is specifically vulnerable to</li>
<li>Cocaine is particularly high-risk — rapid, intense dopamine surge; associated with BD1 mixed states and psychosis</li>
<li>Even prescribed stimulants (for comorbid ADHD) can destabilise mood — dose carefully, monitor closely; require mood stabiliser cover</li>
</ul>
<p><strong>Caffeine:</strong> Not a major clinical issue for most — moderate caffeine (1–2 cups coffee) is unlikely to trigger episodes. However, during prodromal phases or when sleep is already disrupted, caffeine is additive to the circadian disruption. Reduce or stop caffeine as one of the first interventions if early warning signs develop.</p>"""
            },
            {
                "id": "bp1_life",
                "title": "Relationships, work, and living well",
                "body": """<p><strong>Recovery — what it looks like and what it asks:</strong> Full recovery from bipolar disorder does not mean freedom from the diagnosis or the need for medication. It means: long periods between episodes; the ability to recognise warning signs and act on them; a meaningful work and social life; and a sense of agency over the illness rather than being defined by it. Many people with BD1 lead highly successful professional and personal lives. The illness does not determine the ceiling.</p>
<p><strong>Disclosure — a personal decision with real trade-offs:</strong></p>
<ul>
<li>You are not legally required to disclose your diagnosis to employers in most contexts in Australia — the exception is roles where impaired judgment poses safety risks to others</li>
<li>Disclosure may enable workplace accommodations (modified hours during difficult periods, working from home, reduced travel) under the Fair Work Act 2009 and Disability Discrimination Act 1992</li>
<li>Stigma about bipolar disorder remains significant; not everyone responds constructively to disclosure</li>
<li>For close relationships, disclosure often reduces conflict by providing context for behaviour during episodes, and allows partners to be part of the relapse plan</li>
</ul>
<p><strong>Driving and medication:</strong> Acute manic episodes impair driving — do not drive when unwell, and be transparent with your treating team. Most mood stabilisers and antipsychotics can cause sedation that impairs driving particularly in the first weeks or on dose increases. In Australia, driving with a prescribed medication is legal as long as driving ability is not actually impaired. Austroads Medical Standards for Licensing are relevant if required by your employer or insurer.</p>
<p><strong>NDIS access:</strong> BD1 may qualify as a disability under the NDIS if it has a substantial and permanent functional impact. Psychosocial supports (support coordination, community participation, skills development) may be funded. Discuss with your treating team if BD1 is significantly impairing your daily functioning.</p>
<p><strong>Advance care directives and Ulysses agreements:</strong> Strongly recommended. A Ulysses agreement is a document written while well specifying what interventions you consent to if you become unwell and lack insight — including hospitalisation, specific medications, and who to involve. It can be shared with your psychiatrist, GP, family, and hospital. It is one of the most autonomy-preserving tools available in BD management.</p>
<p><strong>Identity and bipolar disorder:</strong> Many people with BD1 report creativity, energy, interpersonal intensity, and drive that they value and associate with the same neurobiology as their illness. This is worth acknowledging. Treatment does not aim to flatten these qualities — it aims to prevent the episodes that harm. The goal is not a smaller life but a stable platform from which to live a full one.</p>"""
            },
            {
                "id": "bp1_resources",
                "title": "Support services and resources (Australia)",
                "body": """<p><strong>SANE Australia — 1800 187 263</strong><br>Australia's largest mental health charity specifically focused on complex mental illness including bipolar disorder. Peer support, information, counselling, carer support, and moderated online community. <a href="https://www.sane.org" target="_blank">sane.org</a></p>
<p><strong>Black Dog Institute</strong><br>Clinical research and education centre at UNSW with extensive publicly available resources on bipolar disorder, mood diary tools, and self-management guides. Evidence-based, Australia-specific. <a href="https://www.blackdoginstitute.org.au" target="_blank">blackdoginstitute.org.au</a></p>
<p><strong>Living With Bipolar Australia (formerly Bipolar Australia)</strong><br>Consumer-run Australian organisation providing peer support, information, and advocacy for people with bipolar disorder and their families. <a href="https://lwbipolar.org.au" target="_blank">lwbipolar.org.au</a></p>
<p><strong>RANZCP Clinical Practice Guidelines for Mood Disorders</strong><br>The authoritative Australian/NZ clinical guidelines, freely available online. For patients who want to understand the evidence basis of their treatment. <a href="https://www.ranzcp.org/clinical-guidelines-publications/clinical-guidelines-publications-detail/cpg-for-mood-disorders" target="_blank">Available at ranzcp.org</a></p>
<p><strong>Mood diary apps — tracking as a clinical tool:</strong></p>
<ul>
<li><strong>eMoods:</strong> Designed specifically for bipolar disorder — tracks mood, sleep, medication, and symptoms with customisable daily ratings; generates PDF reports to share with your psychiatrist. Free with optional premium. <a href="https://emoodtracker.com" target="_blank">emoodtracker.com</a></li>
<li><strong>Daylio:</strong> Simple icon-based daily mood and activity journal — lower-barrier entry. Useful for people who find detailed journalling difficult during low mood.</li>
<li><strong>Optimism:</strong> Comprehensive self-management app for mood disorders — mood tracking, wellness plan, relapse identification. <a href="https://optimism.net.au" target="_blank">optimism.net.au</a></li>
</ul>
<p><strong>Carers Australia — 1800 242 636</strong><br>Support for carers and family members of people with mental illness including bipolar disorder. Carer counselling, respite information, peer support. <a href="https://www.carersaustralia.com.au" target="_blank">carersaustralia.com.au</a></p>
<p><strong>Headspace / Head to Health</strong><br>Digital mental health entry point for Australians — service finder, self-help resources, telehealth connections. <a href="https://www.headtohealth.gov.au" target="_blank">headtohealth.gov.au</a></p>
<p><strong>Lifeline — 13 11 14</strong><br>24/7 crisis support. For urgent suicidal ideation or distress that cannot wait for regular appointment.</p>
<p><strong>000 — emergency</strong><br>For acute psychiatric emergencies including florid mania with risk to self or others.</p>"""
            }
        ]
    }
]

def build_items_js(groups):
    lines = []
    lines.append("var BP1_PE_GROUPS=[")
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
<title>Bipolar 1 Disorder Psychoeducation — Dr Benjamin Murrie</title>
<style>
:root{--bg:#f0f2f5;--surface:#fff;--border:#e2e6ed;--text:#1a1d23;--muted:#6b7280;--bp1:#a21caf;--bp1-bg:#fdf4ff;--bp1-dark:#701a75;--bp1-mid:#c026d3;--navy:#0f172a;--sans:-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--text);font-size:15px;min-height:100vh}
.topbar{background:var(--navy);padding:10px 14px;border-bottom:3px solid var(--bp1);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.topbar-title{font-size:13px;font-weight:800;color:#f5d0fe;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ti{background:#1e293b;border:1px solid #334155;color:#f1f5f9;padding:5px 9px;border-radius:7px;font:inherit;font-size:13px;min-width:0}
.ti::placeholder{color:#64748b}
.ti:focus{outline:1px solid var(--bp1);background:#243349}
.content{max-width:1000px;margin:0 auto;padding:14px 12px 40px}
.condition-block{margin-bottom:14px;border-radius:10px;overflow:hidden;border:1px solid var(--border)}
.condition-header{padding:10px 14px;font:700 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:10px;background:var(--bp1-dark)}
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
.pe-body th{background:#fdf4ff;padding:5px 8px;text-align:left;border:1px solid var(--border);font-size:11px}
.pe-body td{padding:4px 8px;border:1px solid var(--border);vertical-align:top}
.pe-body a{color:var(--bp1-mid)}
.pe-section.bp1-done{background:#fdf4ff}
.pe-section.bp1-done .pe-tick-btn{color:var(--bp1)}
.pe-section.pe-optional{opacity:.88}
.export-row{background:#fff;border:1px solid var(--border);border-radius:10px;padding:11px 14px;margin-bottom:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.export-row .ex-label{font:700 12px var(--sans);color:var(--muted);flex-shrink:0;white-space:nowrap}
.abtn{padding:7px 14px;border-radius:8px;border:1.5px solid var(--border);background:#fff;color:var(--text);font:600 12px var(--sans);cursor:pointer;transition:background .1s,border-color .1s}
.abtn:hover{background:#f3f4f6;border-color:#94a3b8}
.abtn.copied{background:#fdf4ff;border-color:#e879f9;color:#701a75}
.preview-wrap{background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.preview-head{background:#f8fafc;border-bottom:1px solid var(--border);padding:9px 14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.preview-head-title{font:700 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.preview-body{padding:22px 26px;font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#111;min-height:100px}
.preview-body .empty-msg{color:var(--muted);font-style:italic;text-align:center;padding:36px 20px;font-size:11pt}
.ho-header{margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e5e7eb}
.ho-pt{font-size:17pt;font-weight:800;color:#0f172a;margin-bottom:2px}
.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:12px}
.ho-group-label{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:14px 0 6px;padding-bottom:3px;border-bottom:2px solid currentColor}
.ho-group-label.bp1-g-core{color:#701a75;border-bottom-color:#701a75}
.ho-group-label.bp1-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.bp1-g-medications{color:#4c1d95;border-bottom-color:#4c1d95}
.ho-group-label.bp1-g-living{color:#0e7490;border-bottom-color:#0e7490}
.ho-topic{margin-bottom:20px;padding:11px 14px;border:1px solid #e5e7eb;border-radius:7px;background:#fefbff}
.ho-topic-title{font-weight:700;font-size:11pt;color:#0f172a;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb}
.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151}
.ho-topic-body p{margin:0 0 6px}
.ho-topic-body p:last-child{margin:0}
.ho-topic-body ul{margin:3px 0 7px 16px}
.ho-topic-body li{margin-bottom:3px}
.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:5px 0 8px}
.ho-topic-body th{background:#fdf4ff;padding:4px 7px;text-align:left;border:1px solid #d1d5db;font-size:9pt}
.ho-topic-body td{padding:3pt 7pt;border:1px solid #d1d5db;vertical-align:top}
.ho-topic-body a{color:#a21caf}
.ho-footer{margin-top:24px;padding-top:12px;border-top:1px solid #e5e7eb;font-size:8.5pt;color:#9ca3af;font-style:italic}
</style>
</head>
<body>
<div class="topbar">
  <span class="topbar-title">Bipolar 1 Disorder Psychoeducation</span>
  <input class="ti" id="ptName" placeholder="Patient name..." style="flex:1;min-width:130px;max-width:210px" oninput="refresh()">
  <input class="ti" id="ptDate" type="date" style="flex:0 0 128px" oninput="refresh()">
  <input class="ti" id="drName" placeholder="Clinician name..." style="flex:1;min-width:130px;max-width:200px" oninput="refresh()">
</div>
<div class="content">
  <div class="condition-block" style="margin-top:12px">
    <div class="condition-header">
      Bipolar 1 Disorder — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll()">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll()">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="bp1-topic-list"></div>
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

var GROUP_COLOR_CLASS={'null':'bp1-g-core','Treatment':'bp1-g-treatment','Medications':'bp1-g-medications','Living Well with Bipolar 1':'bp1-g-living'};

function renderTopics(){
  var el=$('bp1-topic-list'); if(!el) return;
  var html='';
  BP1_PE_GROUPS.forEach(function(g){
    if(g.label) html+='<div class="pe-group-label">'+(g.optional?'<span style="font-size:9px;opacity:.6;font-weight:600;margin-right:4px">OPTIONAL</span>':'')+esc(g.label)+'</div>';
    g.items.forEach(function(item){
      var done=!!sel[item.id];
      html+='<div class="pe-section'+(done?' bp1-done':'')+(g.optional?' pe-optional':'')+'" data-id="'+item.id+'">';
      html+='<div class="pe-header"><span class="pe-tick-btn">'+(done?'&#9745;':'&#9744;')+'</span>';
      html+='<span class="pe-title">'+esc(item.title)+'</span>';
      html+='<span class="pe-arrow">&#9658;</span></div>';
      html+='<div class="pe-body">'+item.body+'</div></div>';
    });
  });
  el.innerHTML=html;
  el.onclick=function(e){
    var sec=e.target.closest('[data-id]'); if(!sec) return;
    var id=sec.getAttribute('data-id');
    if(e.target.classList.contains('pe-tick-btn')){
      e.stopPropagation();
      sel[id]=!sel[id];
      sec.classList.toggle('bp1-done',!!sel[id]);
      sec.querySelector('.pe-tick-btn').innerHTML=sel[id]?'&#9745;':'&#9744;';
      refresh();
    } else {
      var hdr=e.target.closest('.pe-header'); if(hdr) sec.classList.toggle('pe-open');
    }
  };
}
function selectAll(){BP1_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){sel[item.id]=true;});});renderTopics();refresh();}
function clearAll(){Object.keys(sel).forEach(function(k){sel[k]=false;});renderTopics();refresh();}

function buildHandout(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var hasAny=false;
  BP1_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){if(sel[item.id])hasAny=true;});});
  if(!hasAny) return null;
  var h='';
  h+='<div class="ho-header">';
  h+='<div class="ho-pt">Psychoeducation Handout — Bipolar 1 Disorder</div>';
  h+='<div class="ho-meta">Patient: <strong>'+esc(name)+'</strong>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <strong>'+esc(dr)+'</strong></div>';
  h+='</div>';
  var currentGroup=null;
  BP1_PE_GROUPS.forEach(function(g){
    g.items.forEach(function(item){
      if(!sel[item.id]) return;
      var gKey=g.label||'null';
      if(gKey!==currentGroup){
        if(g.label){
          var cls=GROUP_COLOR_CLASS[g.label]||'bp1-g-core';
          h+='<div class="ho-group-label '+cls+'">'+esc(g.label)+'</div>';
        }
        currentGroup=gKey;
      }
      h+='<div class="ho-topic">';
      h+='<div class="ho-topic-title">'+esc(item.title)+'</div>';
      h+='<div class="ho-topic-body">'+item.body+'</div>';
      h+='</div>';
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
    '.ho-group-label{font-size:8.5pt;font-weight:bold;text-transform:uppercase;letter-spacing:.06em;margin:11pt 0 5pt;padding-bottom:2pt;border-bottom:1.5pt solid currentColor;}'+
    '.ho-group-label.bp1-g-core{color:#701a75;}.ho-group-label.bp1-g-treatment{color:#1e3a5f;}.ho-group-label.bp1-g-medications{color:#4c1d95;}.ho-group-label.bp1-g-living{color:#0e7490;}'+
    '.ho-topic{margin-bottom:20pt;padding:10pt 13pt;border:1pt solid #e5e7eb;background:#fefbff;}'+
    '.ho-topic-title{font-weight:bold;font-size:11pt;color:#0f172a;margin:0 0 5pt;padding-bottom:4pt;border-bottom:1pt solid #e5e7eb;}'+
    '.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151;}'+
    '.ho-topic-body p{margin:0 0 5pt;}.ho-topic-body ul{margin:3pt 0 6pt 14pt;}.ho-topic-body li{margin-bottom:3pt;}'+
    '.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9pt;margin:5pt 0 8pt;}'+
    '.ho-topic-body th{background:#fdf4ff;padding:4pt 6pt;text-align:left;border:1pt solid #d1d5db;font-size:8.5pt;}'+
    '.ho-topic-body td{padding:3pt 6pt;border:1pt solid #d1d5db;vertical-align:top;}'+
    '.ho-footer{margin-top:20pt;padding-top:10pt;border-top:1pt solid #e5e7eb;font-size:8pt;color:#9ca3af;font-style:italic;}'+
    '</style></head><body>'+html+'</body></html>';
}

function dlDocx(){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected.');return;}
  var name=(f('ptName')||'Patient').replace(/[^a-zA-Z0-9]/g,'_');
  var blob=new Blob(['﻿'+docx],{type:'application/msword;charset=utf-8'});
  var url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='BP1_Psychoeducation_'+name+'.doc';
  document.body.appendChild(a);a.click();document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);},2000);
  flash($('btn-docx'),'Downloaded!');
}
function copyPlain(btn){
  var pv=$('preview');
  if(!buildHandout()){alert('No topics selected.');return;}
  navigator.clipboard.writeText(pv.innerText||pv.textContent).then(function(){flash(btn,'Copied!');}).catch(function(){});
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

import os
BASE = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(BASE, 'bp1-psychoeducation.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print("Done.")
