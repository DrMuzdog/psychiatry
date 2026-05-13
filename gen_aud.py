#!/usr/bin/env python3
"""Generate aud-psychoeducation.html — Alcohol Use Disorder psychoeducation tool."""

def esc(s):
    return s.replace("'", "\\'")

groups = [
    {
        "label": None,
        "optional": False,
        "items": [
            {
                "id": "what_aud",
                "title": "What is Alcohol Use Disorder?",
                "body": """<p><strong>Definition:</strong> Alcohol Use Disorder (AUD) is a chronic brain condition characterised by a problematic pattern of alcohol use causing clinically significant impairment or distress. It is diagnosed on a spectrum of severity using eleven DSM-5 criteria:</p>
<ul>
<li><strong>Mild AUD:</strong> 2–3 criteria met</li>
<li><strong>Moderate AUD:</strong> 4–5 criteria met</li>
<li><strong>Severe AUD:</strong> 6 or more criteria met</li>
</ul>
<p><strong>The eleven criteria</strong> include: drinking more or longer than intended; persistent unsuccessful efforts to cut down; significant time spent obtaining, using, or recovering from alcohol; craving; failure to fulfil major role obligations; continued use despite persistent social or interpersonal problems it causes; giving up important activities; use in physically hazardous situations; continued use despite knowledge of a physical or psychological problem caused by alcohol; tolerance (needing more to achieve the same effect); and withdrawal symptoms when not drinking.</p>
<p><strong>Not a moral failing:</strong> AUD is a neurobiological condition with strong genetic loading (heritability approximately 50%) and measurable changes in brain structure and function. It is not a character flaw, weakness, or lifestyle choice. This distinction is clinically important because shame and self-blame are powerful barriers to help-seeking and treatment engagement, and they are not accurate.</p>
<p><strong>Prevalence:</strong> Approximately 10–15% of Australians will meet criteria for AUD at some point in their lifetime. Roughly 5–6% of Australian adults meet criteria at any given time. AUD is more common in men, though rates in women are rising and women tend to develop complications more rapidly for equivalent consumption (telescoping phenomenon).</p>
<p><strong>The spectrum matters:</strong> A person does not need to drink daily, drink spirits, or have lost their job to have AUD. Weekend binge drinking with loss of control, repeated failed attempts to moderate, and continued use despite relationship or health consequences all satisfy criteria at various severity levels.</p>"""
            },
            {
                "id": "aud_neuroscience",
                "title": "The neuroscience of addiction — why willpower is not the problem",
                "body": """<p><strong>The mesolimbic dopamine system:</strong> Alcohol — like all addictive substances — acts on the brain's reward circuitry. The ventral tegmental area (VTA) projects dopamine to the nucleus accumbens (reward hub) and prefrontal cortex. Alcohol triggers a surge of dopamine that the brain codes as highly significant — producing intense pleasure, relief, and a powerful signal to repeat the behaviour.</p>
<p><strong>Neuroadaptation — the trap:</strong> With regular heavy use, the brain adapts to compensate for constant stimulation:</p>
<ul>
<li>Dopamine receptors downregulate — less reward from the same amount</li>
<li>GABA (the brain's main inhibitory neurotransmitter) activity is chronically suppressed</li>
<li>Glutamate (excitatory, NMDA) receptors upregulate to compensate</li>
<li>The brain becomes dependent on alcohol simply to feel normal</li>
</ul>
<p>The result: alcohol produces less pleasure over time (tolerance) but stopping produces severe dysphoria, anxiety, and — because of excitatory rebound — withdrawal seizures. The person is now drinking primarily to avoid withdrawal, not to feel good.</p>
<p><strong>Prefrontal hypoactivity:</strong> Chronic alcohol use reduces grey matter volume and activity in the prefrontal cortex — the region responsible for impulse control, long-term planning, and weighing consequences. Neuroimaging consistently demonstrates this. The implication is that the brain regions needed to choose not to drink are impaired by the drinking itself. Willpower is a prefrontal function. Asking someone to use willpower against a condition that damages willpower is structurally ineffective.</p>
<p><strong>Conditioned craving:</strong> Through Pavlovian conditioning, cues associated with drinking (specific places, emotional states, social contexts, smells, times of day) trigger automatic craving responses that do not require conscious decision-making. These conditioned responses can persist years after cessation and are activated without the person choosing to think about alcohol.</p>
<p><strong>The clinical implication:</strong> Medications that target the dopamine, GABA, and glutamate systems are rational biological interventions for a biological condition. This is not a substitution or a crutch — it is the same logic as treating hypertension with antihypertensives rather than asking the patient to try harder.</p>"""
            },
            {
                "id": "aud_withdrawal",
                "title": "Alcohol withdrawal — why stopping suddenly can be dangerous",
                "body": """<p><strong>Critical safety information:</strong> Unlike withdrawal from opioids, cannabis, or stimulants, alcohol withdrawal can be fatal. The chronic upregulation of excitatory glutamate systems means that removing alcohol suddenly leaves excitatory activity unchecked. This is not a rare edge case — it is a predictable consequence of physical dependence.</p>
<p><strong>Withdrawal timeline:</strong></p>
<table>
<tr><th>Time after last drink</th><th>Typical features</th></tr>
<tr><td>6–12 hours</td><td>Tremor, anxiety, diaphoresis, nausea and vomiting, tachycardia, hypertension, insomnia</td></tr>
<tr><td>12–24 hours</td><td>Symptoms peak for mild–moderate cases; alcoholic hallucinosis possible (visual/tactile/auditory — patient remains lucid and oriented)</td></tr>
<tr><td>24–48 hours</td><td>Generalised tonic-clonic seizure risk — usually brief, may be status epilepticus</td></tr>
<tr><td>48–96 hours</td><td>Delirium tremens — agitation, disorientation, fever, autonomic instability; untreated mortality up to 15%, treated 1–3%</td></tr>
</table>
<p><strong>Risk factors for severe withdrawal:</strong> Previous withdrawal seizures or DTs; high daily consumption (>15 standard drinks/day); duration of heavy use; concurrent medical illness; liver disease; electrolyte abnormalities; age; concurrent sedative use; inadequate nutrition.</p>
<p><strong>Clinical assessment — CIWA-Ar:</strong> The Clinical Institute Withdrawal Assessment for Alcohol (revised) is the standard validated tool. Ten items assessed on scales of 0–7 (nausea/vomiting, tremor, sweats, anxiety, agitation, sensory disturbances, headache) plus orientation (0–4). Scores: &lt;10 mild; 10–14 moderate; ≥15 severe. CIWA-Ar &lt;10 often manageable in community with careful monitoring; ≥15 warrants inpatient admission.</p>
<p><strong>Management:</strong> Benzodiazepines (diazepam or chlordiazepoxide) are the evidence-based treatment for moderate-to-severe withdrawal — typically symptom-triggered dosing guided by CIWA-Ar. <strong>Thiamine supplementation is essential</strong> — Wernicke encephalopathy (ophthalmoplegia, ataxia, encephalopathy) can be precipitated in malnourished drinkers. IV Pabrinex (thiamine) must be given before glucose loads in any malnourished patient with suspected alcohol dependence.</p>
<p><strong>Home vs inpatient detox:</strong> Home detox is appropriate for mild withdrawal with good social support, no prior seizures or DTs, no significant medical comorbidity, and willingness to attend daily monitoring. Inpatient admission should be offered for: prior seizures or DTs; CIWA-Ar ≥15; inadequate social support; significant medical or psychiatric comorbidity; failed prior community attempts.</p>
<p><strong>Do not advise abrupt cessation</strong> to a physically dependent person without a medical withdrawal management plan in place.</p>"""
            },
            {
                "id": "aud_medical",
                "title": "Medical consequences — what is at stake",
                "body": """<p><strong>Liver:</strong> The progression of alcohol-related liver disease: fatty liver (steatosis — reversible with abstinence) → alcoholic hepatitis (inflammation, can be severe and life-threatening) → cirrhosis (irreversible fibrosis, portal hypertension, hepatic failure). Cirrhosis is present in approximately 10–20% of people with severe AUD and substantially increases risk of hepatocellular carcinoma. Even clinically silent liver disease affects medication metabolism — particularly relevant to naltrexone prescribing (see Medications).</p>
<p><strong>Wernicke-Korsakoff Syndrome:</strong> A thiamine (vitamin B1) deficiency syndrome almost specific to alcohol-related malnutrition. Wernicke encephalopathy is acute and reversible if treated promptly — the classic triad is ophthalmoplegia, ataxia, and encephalopathy, though the full triad is present in fewer than 20% of cases. Untreated, it progresses to Korsakoff syndrome: dense anterograde amnesia with confabulation that is largely irreversible. All people with AUD should receive thiamine supplementation.</p>
<p><strong>Cardiovascular:</strong> Dose-dependent association with atrial fibrillation, alcoholic cardiomyopathy, hypertension, and haemorrhagic stroke. Holiday heart syndrome (AF with acute heavy use) is well described. Modest cardioprotective effects at very low consumption may exist but are absent above approximately 1–2 standard drinks/day, and the overall health burden is negative at any level above this.</p>
<p><strong>Neurological:</strong> Cerebral atrophy (measurable on MRI), peripheral neuropathy (length-dependent, partially reversible with abstinence and thiamine), cerebellar degeneration (gait ataxia), and varying degrees of cognitive impairment affecting executive function, memory, and processing speed. Much cognitive impairment improves substantially with sustained abstinence — the brain has significant recovery capacity, particularly in the first 1–2 years.</p>
<p><strong>Cancer:</strong> Alcohol is a Group 1 IARC carcinogen with clear causal relationships to oropharyngeal, laryngeal, oesophageal, liver, colorectal, and breast cancer. Risk is dose-dependent with no established safe threshold specifically for cancer risk.</p>
<p><strong>Other:</strong> Pancreatitis (acute and chronic); immune suppression; sleep disruption (suppresses REM, causes sleep fragmentation and rebound insomnia on cessation); sexual dysfunction; foetal alcohol spectrum disorders (safe level during pregnancy is zero).</p>"""
            },
            {
                "id": "aud_mental_health",
                "title": "Mental health and alcohol — a bidirectional relationship",
                "body": """<p><strong>The bidirectional trap:</strong> Alcohol and mental health conditions powerfully influence each other in both directions. Approximately 50% of people with AUD have a co-occurring mental health condition. Untangling cause, consequence, and independent comorbidity requires careful timing of assessment and should not be rushed.</p>
<p><strong>Alcohol worsens depression and anxiety:</strong> Despite its immediate anxiolytic and sedative effects, chronic alcohol use progressively worsens baseline mood and anxiety through disruption of GABA, serotonin, and dopamine systems. People who drink to manage anxiety or depression typically find their untreated baseline deteriorates over time, requiring escalating doses to achieve the same effect. The relief is real — the long-term consequence is worse.</p>
<p><strong>Diagnostic timing:</strong> Many depressive and anxiety symptoms are directly produced by alcohol and resolve substantially with abstinence. Standard practice is to reassess mental health conditions after 2–4 weeks of abstinence before diagnosing an independent mood or anxiety disorder. Initiating antidepressants in the context of active heavy drinking is often ineffective and may be unnecessary.</p>
<p><strong>Suicide risk:</strong> AUD is one of the strongest modifiable risk factors for suicide. People with AUD have approximately 4–8 times the age-matched suicide rate. Risk is elevated during: acute intoxication (impaired impulse control), early abstinence (depressive rebound, dysphoria), and periods of significant psychosocial loss (relationship breakdown, employment loss, legal consequences). Suicide risk assessment should be routine at every contact in active AUD.</p>
<p><strong>PTSD and AUD:</strong> Co-occur at high rates — up to 50% of people with severe AUD have clinically significant trauma histories. The relationship is bidirectional: trauma increases AUD risk (self-medication of hyperarousal), and AUD increases trauma exposure. Integrated concurrent treatment of both conditions outperforms sequential treatment. Several medications used for AUD (naltrexone, prazosin, some off-label agents) have evidence in PTSD too.</p>
<p><strong>Stimulant use and AUD:</strong> Alcohol and stimulants (cocaine, amphetamines) co-occur at high rates, partly because stimulants counteract sedation and permit more drinking. Cocaethylene — formed from concurrent cocaine and alcohol use in the liver — is more cardiotoxic than either substance alone and has a longer half-life.</p>"""
            }
        ]
    },
    {
        "label": "Treatment",
        "optional": False,
        "items": [
            {
                "id": "aud_treatment_overview",
                "title": "Treatment — what works",
                "body": """<p><strong>AUD is treatable.</strong> Across severity levels, evidence-based interventions reduce consumption, prevent relapse, and improve medical and psychological outcomes. Treatment works best when it combines pharmacological and psychological approaches and when it is sustained — AUD is a chronic condition, and most people benefit from ongoing rather than episodic care.</p>
<p><strong>Levels of care:</strong></p>
<table>
<tr><th>Setting</th><th>Appropriate for</th></tr>
<tr><td>Brief intervention (GP, ED)</td><td>Hazardous/harmful use; mild AUD; early presentation; raising awareness</td></tr>
<tr><td>Outpatient counselling + medication</td><td>Mild–moderate AUD; adequate social support; motivated; no severe withdrawal risk</td></tr>
<tr><td>Intensive outpatient programme (IOP)</td><td>Moderate–severe AUD; more structure needed; maintained community life</td></tr>
<tr><td>Residential rehabilitation</td><td>Severe AUD; poor social support; high relapse risk; failed outpatient; complex comorbidity</td></tr>
<tr><td>Medically supervised withdrawal (inpatient)</td><td>Severe dependence; prior seizures or DTs; significant medical comorbidity</td></tr>
</table>
<p><strong>Relapse is not failure:</strong> Most people with AUD make multiple attempts before achieving sustained remission. The average person makes 4–5 serious attempts before long-term recovery. Relapse should be understood as a normal feature of a chronic condition requiring recalibration — not as evidence that treatment does not work or that the person is unwilling. What matters is re-engagement, not absence of relapse.</p>
<p><strong>Long-term outcomes:</strong> With sustained treatment engagement, approximately 30–50% of people with AUD achieve long-term remission (abstinence or low-risk drinking). A further substantial proportion achieve significant harm reduction. Prognosis is better than pessimism suggests and improves with treatment engagement.</p>"""
            },
            {
                "id": "aud_withdrawal_mgmt",
                "title": "Managing withdrawal safely — detoxification",
                "body": """<p><strong>Goals of medically supervised withdrawal:</strong> Safe management of acute withdrawal symptoms; prevention of seizures and delirium tremens; thiamine repletion; preparation for ongoing rehabilitation; not an endpoint in itself. Detoxification without subsequent treatment has a very high relapse rate — it is a starting point, not a destination.</p>
<p><strong>Standard pharmacological approach — benzodiazepines:</strong> Diazepam and chlordiazepoxide are first-line. Both are long-acting and provide smooth coverage. Symptom-triggered dosing guided by CIWA-Ar is preferred over fixed-schedule dosing and uses less medication overall.</p>
<p><strong>Sample diazepam protocol (community — mild withdrawal, CIWA-Ar &lt;10):</strong></p>
<table>
<tr><th>Day</th><th>Diazepam dose</th></tr>
<tr><td>Day 1</td><td>10mg QID (40mg total)</td></tr>
<tr><td>Day 2</td><td>10mg TID (30mg total)</td></tr>
<tr><td>Day 3</td><td>10mg BD (20mg total)</td></tr>
<tr><td>Day 4</td><td>10mg nocte</td></tr>
<tr><td>Day 5</td><td>5mg nocte, then cease</td></tr>
</table>
<p>Higher initial doses and longer tapers are required for moderate–severe withdrawal (CIWA-Ar 10–18: day 1 doses 60–100mg total). Inpatient CIWA-triggered protocols use diazepam 20mg Q1–2H while CIWA-Ar ≥10.</p>
<p><strong>Thiamine — non-negotiable:</strong> All people undergoing withdrawal should receive thiamine. For community detox: thiamine 100mg TID orally. For inpatient or malnourished patients: IV Pabrinex (250mg thiamine + other B vitamins) for at least 3–5 days. <strong>Never administer IV glucose to a thiamine-depleted patient before thiamine</strong> — this can precipitate acute Wernicke encephalopathy.</p>
<p><strong>Alternatives to benzodiazepines:</strong> For patients with significant benzodiazepine misuse history or where long-acting benzos are problematic — carbamazepine (off-label, titrated over 5–7 days) has evidence for mild–moderate withdrawal and does not have misuse potential. Gabapentin is increasingly used (see Medications). Phenobarbitone is used in specialist settings for refractory withdrawal.</p>
<p><strong>After withdrawal:</strong> The completion of detox is when pharmacological treatment for relapse prevention should begin. Initiating naltrexone or acamprosate at the completion of withdrawal is associated with significantly better outcomes than delaying until "stable."</p>"""
            },
            {
                "id": "aud_goals",
                "title": "Setting goals — abstinence, reduction, or controlled drinking?",
                "body": """<p><strong>Both abstinence and reduction are legitimate goals.</strong> The traditional view that abstinence is the only acceptable goal for AUD has been substantially revised in evidence-based practice. For many people — particularly those with mild-to-moderate AUD, significant life reasons to continue some drinking, or who are unwilling to commit to abstinence — a harm reduction goal is clinically valid and substantially better than no treatment.</p>
<p><strong>Arguments for abstinence as a goal:</strong></p>
<ul>
<li>Best outcomes in severe AUD and physical dependence</li>
<li>Removes cue exposure and conditioned responses entirely</li>
<li>Required for some medications (disulfiram; acamprosate works best in abstinence)</li>
<li>Necessary with significant liver disease, pregnancy, certain medications, or work roles</li>
<li>Supported by AA, 12-step programmes, and many residential services</li>
</ul>
<p><strong>Arguments for a reduction/moderation goal:</strong></p>
<ul>
<li>More acceptable to many people, improving initial engagement</li>
<li>The Sinclair Method with naltrexone (see Medications) is specifically designed for controlled drinking</li>
<li>NHMRC guidelines acknowledge that reduced drinking below low-risk thresholds is a valid treatment outcome</li>
<li>Harm reduction has strong evidence: even partial reduction in consumption significantly reduces medical and social harm</li>
<li>Can be a stepping stone to later abstinence if moderation proves untenable</li>
</ul>
<p><strong>Australian low-risk drinking guidelines (NHMRC 2020):</strong> No more than 10 standard drinks per week; no more than 4 standard drinks on any single day. One Australian standard drink = 10g of alcohol (e.g., 285mL full-strength beer, 100mL wine, 30mL spirits).</p>
<p><strong>The clinical conversation:</strong> Explore goals without pre-determining them. People whose initial goal is moderation who find it consistently unachievable often shift to abstinence on their own timeline. Forcing abstinence as the only option commonly drives people out of treatment entirely — which is the worst outcome.</p>"""
            },
            {
                "id": "aud_psychology",
                "title": "Psychological therapies for AUD",
                "body": """<p><strong>Cognitive Behavioural Therapy (CBT):</strong> The most extensively evidence-based psychological intervention for AUD. Identifies and modifies thoughts, beliefs, and behaviours that trigger and maintain drinking. Core components: functional analysis of drinking (antecedents, behaviour, consequences), identifying high-risk situations, coping skills training, relapse prevention planning, addressing unhelpful cognitions about drinking and self-efficacy. Typically 12–20 sessions. Can be individual or group-based.</p>
<p><strong>Motivational Interviewing (MI):</strong> A collaborative, person-centred approach that elicits and strengthens the person's own motivation to change. Particularly effective in early treatment and with ambivalent individuals. Core techniques: reflective listening, developing discrepancy between current behaviour and stated values, rolling with resistance, supporting self-efficacy. Strong evidence as a prelude or complement to other treatments, particularly in brief intervention settings.</p>
<p><strong>Alcoholics Anonymous (AA) and 12-Step:</strong> The most widely available mutual support programme globally. Evidence is mixed in controlled trials but consistently positive in observational studies and meta-analyses of participation. Active AA attendance is associated with better long-term outcomes than non-attendance. Key mechanisms: social support, accountability, identity change, spiritual framework (though secular adaptations exist). No referral required; meeting attendance is free and broadly available.</p>
<p><strong>SMART Recovery:</strong> CBT-based secular alternative to AA. Uses evidence-based tools including cost-benefit analysis, coping with urges, managing thoughts and emotions, and building a balanced lifestyle. Available as face-to-face meetings and online. Particularly suitable for people who do not identify with the 12-step spiritual framework. <a href="https://www.smartrecovery.org.au" target="_blank">smartrecovery.org.au</a></p>
<p><strong>CRAFT (Community Reinforcement and Family Training):</strong> Evidence-based programme for family members and partners of people with AUD who are not yet engaging in treatment. Teaches communication skills, reinforcement of non-drinking behaviour, allowing natural consequences, and self-care. Outperforms Al-Anon and confrontational approaches in getting the person with AUD into treatment. Available through some AOD services and trained therapists.</p>
<p><strong>Residential rehabilitation:</strong> Intensive programmes providing a structured, alcohol-free environment for 28 days to 12 months. Most effective for people with severe AUD, poor social support, or repeated outpatient failures. The social network replacement and structured daily routine are often as important as the formal treatment components.</p>"""
            }
        ]
    },
    {
        "label": "Medications",
        "optional": False,
        "items": [
            {
                "id": "med_naltrexone",
                "title": "Naltrexone (oral) — ReVia | PBS listed",
                "body": """<p><strong>Class:</strong> Opioid receptor antagonist (μ, κ, δ). <strong>PBS status:</strong> Yes — Section 85, Authority Required for alcohol dependence in Australia. <strong>Brand:</strong> ReVia (50mg tablets); generics available.</p>
<p><strong>Mechanism:</strong> Blocks μ-opioid receptors in the mesolimbic system, preventing the dopamine surge and subjective reward (euphoria, relaxation) that alcohol produces. Drinking on naltrexone does not produce the usual reward signal — over time, the conditioned association between drinking and reward extinguishes.</p>
<p><strong>Evidence:</strong> One of the best-evidenced pharmacotherapies for AUD. NNT approximately 7 for preventing return to heavy drinking (Cochrane 2010). Most effective in reducing heavy drinking days and relapse to heavy drinking; less robust for maintaining abstinence compared to acamprosate.</p>
<p><strong>Standard dosing:</strong></p>
<table>
<tr><th>Approach</th><th>Dose</th><th>Notes</th></tr>
<tr><td>Standard daily</td><td>50mg once daily</td><td>Take with food to reduce nausea</td></tr>
<tr><td>Tolerability titration</td><td>25mg daily × 1 week, then 50mg daily</td><td>Reduces initial nausea; useful in sensitive patients</td></tr>
<tr><td>Sinclair Method (TSM)</td><td>50mg, taken 1–2 hours before drinking</td><td>Not taken on non-drinking days; see below</td></tr>
</table>
<p><strong>The Sinclair Method (Targeted/Pharmacological Extinction):</strong> Developed by Dr David Sinclair; extensively validated in Finland. The rationale is pharmacological extinction: take naltrexone before planned drinking, continue drinking, but the reward is blocked. Over weeks to months, the conditioned craving extinguishes — most patients reduce consumption to low-risk levels or achieve abstinence without being instructed to stop. Finnish trials showed approximately 78% of patients achieved low-risk drinking or abstinence over 12 months. Important practical point: naltrexone is taken ONLY on days the person plans to drink, 1–2 hours before the first drink. This approach is compatible with harm reduction goals and is supported by strong evidence, though less well-known in Australian practice.</p>
<p><strong>Contraindications:</strong></p>
<ul>
<li><strong>Absolute:</strong> Current opioid use or dependence (will precipitate acute withdrawal); acute hepatitis or liver failure; known hypersensitivity</li>
<li><strong>Relative:</strong> Chronic pain managed with opioid analgesia (requires careful discussion — opioid analgesics will be ineffective); liver disease (can use if LFTs &lt;3–5× ULN; monitor closely)</li>
</ul>
<p><strong>Side effects:</strong> Nausea (most common, ~30%, usually resolves within 1–2 weeks; take with food); headache; fatigue; dysphoria/anhedonia (the same mechanism that blocks alcohol reward can dull normal reward in some patients — typically dose-dependent and often improves); decreased libido; abdominal pain; insomnia.</p>
<p><strong>Monitoring:</strong> LFTs at baseline, 1 month, 3 months, then 6-monthly. Can prescribe with liver disease if LFTs &lt;3–5× ULN — not absolutely contraindicated. Warn patient not to take opioid analgesics, codeine-containing preparations, or tramadol while on naltrexone.</p>
<p><strong>Duration:</strong> Minimum 3–6 months; most benefit from 12 months or longer. Relapse risk increases on cessation — discuss tapering vs continuing indefinitely in patients with recurrent relapse history.</p>"""
            },
            {
                "id": "med_naltrexone_lai",
                "title": "Naltrexone long-acting injection — Vivitrol | not PBS listed",
                "body": """<p><strong>Class:</strong> Extended-release opioid antagonist (IM microsphere formulation). <strong>PBS status:</strong> Not listed in Australia — approximate cost $800–1,200/month privately. Widely used in the US where it is PBS equivalent. <strong>Brand:</strong> Vivitrol (380mg/4mL suspension for IM injection).</p>
<p><strong>Mechanism:</strong> Identical to oral naltrexone — μ-opioid receptor antagonism blocking alcohol's reward signal — but delivered as a monthly intramuscular injection into the gluteal muscle. Peak plasma concentration at approximately 2 hours post-injection; therapeutic levels maintained for 28–30 days.</p>
<p><strong>Key advantages over oral formulation:</strong></p>
<ul>
<li><strong>Adherence:</strong> Eliminates the daily decision to take medication — the single most important barrier to oral naltrexone effectiveness</li>
<li><strong>First-pass bypass:</strong> Avoids hepatic first-pass metabolism, potentially safer in mild-to-moderate liver disease</li>
<li><strong>Removes ambivalence at the point of craving:</strong> Patient who has received injection cannot decide not to take medication when craving is high</li>
<li><strong>Stigma reduction:</strong> Some patients find monthly clinic attendance more acceptable than daily visible pill-taking</li>
</ul>
<p><strong>Dosing:</strong> 380mg IM into the gluteal muscle (alternate sides) every 4 weeks. Administered by a healthcare provider. Injection site must be into the muscle (not subcutaneous — can cause tissue necrosis). Use the full 4mL vial mixed as directed in kit.</p>
<p><strong>Pre-treatment requirements:</strong> Must be opioid-free for at least 7–10 days before first injection (longer for long-acting opioids — buprenorphine 7–10 days, methadone 10–14+ days). Conduct naloxone challenge (0.4–0.8mg IV/SC) if opioid-free period is uncertain.</p>
<p><strong>Contraindications:</strong> As per oral naltrexone. Additional: active injection site infection; BMI extremes may affect injection depth and absorption.</p>
<p><strong>Side effects:</strong> Injection site reactions (pain, induration, bruising — usually resolve within 2 weeks; rarely severe necrosis); nausea; fatigue; decreased appetite. Psychiatric effects: depression has been reported — monitor, though evidence for causal relationship is limited.</p>
<p><strong>Clinical considerations:</strong> Emergency opioid analgesia will be ineffective for the 28-day duration. Inform all treating providers and consider medical alert card. In genuine opioid analgesic emergencies, regional anaesthesia is preferred; if opioids are unavoidable, high doses may be needed and respiratory monitoring is essential.</p>
<p><strong>Cost barrier:</strong> The main limitation in Australia. Some private health insurers cover part of the cost. Worth discussing for patients with high relapse rates on oral formulations, those with significant pill-taking non-adherence, or those with high treatment stakes (employment, custody, legal).</p>"""
            },
            {
                "id": "med_acamprosate",
                "title": "Acamprosate — Campral | PBS listed",
                "body": """<p><strong>Class:</strong> GABA/glutamate modulator. <strong>PBS status:</strong> Yes — listed in Australia for maintenance of abstinence in alcohol-dependent patients. <strong>Brand:</strong> Campral (333mg enteric-coated tablets).</p>
<p><strong>Mechanism:</strong> Acamprosate modulates NMDA glutamate receptor activity and potentiates GABA transmission — essentially normalising the excitatory/inhibitory imbalance that chronic alcohol use creates. The clinical effect is reduction in the protracted abstinence syndrome: the anxiety, dysphoria, sleep disturbance, and craving that persist for weeks to months after acute withdrawal and drive late relapse. It does not produce euphoria and has no misuse potential.</p>
<p><strong>Evidence:</strong> Most effective for maintaining abstinence (NNT ~9 for any abstinence; NNT ~7 for sustained abstinence). Less effective for reducing heavy drinking days compared to naltrexone. Works best when started immediately after completing withdrawal and maintained for 6–12 months.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Weight</th><th>Dose</th><th>Regimen</th></tr>
<tr><td>≥60 kg</td><td>666mg (2 × 333mg tablets)</td><td>Three times daily (with meals) — 6 tablets/day total</td></tr>
<tr><td>&lt;60 kg</td><td>333mg (1 × 333mg tablet)</td><td>Three times daily — 3 tablets/day total</td></tr>
</table>
<p><strong>Timing:</strong> Start as soon as abstinence is established (ideally within 24–48 hours of completing withdrawal management). Can be started even if the patient has a minor slip — unlike disulfiram, acamprosate does not react with alcohol.</p>
<p><strong>Contraindications:</strong> Severe renal impairment (eGFR &lt;30 mL/min) — acamprosate is renally excreted without hepatic metabolism. Dose reduce if eGFR 30–60 (use lower dose regimen regardless of weight). <strong>Importantly: no liver metabolism — safe to use in liver disease, including cirrhosis.</strong> This makes acamprosate preferable to naltrexone when hepatic impairment is a concern.</p>
<p><strong>Side effects:</strong> Diarrhoea (most common, usually mild and self-limiting, improves after first 1–2 weeks); nausea; abdominal discomfort; pruritus. Generally very well tolerated — discontinuation rates due to side effects are low in trials.</p>
<p><strong>Monitoring:</strong> Renal function (eGFR) at baseline. No LFT monitoring required. Review efficacy at 4–6 weeks.</p>
<p><strong>Combination with naltrexone:</strong> The COMBINE study (2006) compared naltrexone, acamprosate, and their combination — combination showed no significant benefit over naltrexone alone in that population. However, in clinical practice, the combination is used for patients who have not responded adequately to monotherapy, and mechanistically the two agents have complementary modes of action. Safe to combine.</p>
<p><strong>Duration:</strong> 6–12 months is standard. Longer for patients with prolonged craving or repeated relapse history.</p>"""
            },
            {
                "id": "med_disulfiram",
                "title": "Disulfiram — Antabuse | not PBS listed",
                "body": """<p><strong>Class:</strong> Aldehyde dehydrogenase inhibitor (aversive agent). <strong>PBS status:</strong> Not currently listed in Australia — available through compounding pharmacies or specialist centres. <strong>Brand:</strong> Antabuse; generic disulfiram available.</p>
<p><strong>Mechanism:</strong> Inhibits aldehyde dehydrogenase (ALDH), the enzyme that metabolises acetaldehyde (the first breakdown product of alcohol). Drinking on disulfiram causes rapid acetaldehyde accumulation — producing the disulfiram-ethanol reaction (DER).</p>
<p><strong>The disulfiram-ethanol reaction (DER):</strong> Within 10–30 minutes of alcohol ingestion, patient experiences: facial flushing, throbbing headache, nausea and vomiting, palpitations, tachycardia, dyspnoea, diaphoresis, hypotension, and severe anxiety. Duration: 30 minutes to several hours depending on amount consumed. Severity is alcohol-dose dependent. Severe DERs can cause arrhythmia, myocardial infarction, respiratory depression, or death — particularly at high alcohol doses or in the presence of cardiovascular disease.</p>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Initiation</th><th>Dose</th></tr>
<tr><td>Minimum time from last drink</td><td>Wait ≥12 hours (24–48 hours is safer) before first dose</td></tr>
<tr><td>Starting dose</td><td>200mg once daily (morning)</td></tr>
<tr><td>Dose range</td><td>100–400mg/day; most patients maintained at 200mg</td></tr>
<tr><td>Duration of DER risk after stopping</td><td>Up to 14 days after last dose</td></tr>
</table>
<p><strong>Contraindications:</strong></p>
<ul>
<li><strong>Absolute:</strong> Severe cardiac disease (ischaemic heart disease, heart failure, arrhythmia); psychosis or severe mental illness; pregnancy; current alcohol use (wait ≥12 hours)</li>
<li><strong>Relative:</strong> Significant hepatic impairment (disulfiram is hepatotoxic — monitor LFTs); diabetes; epilepsy; peripheral neuropathy; renal impairment; age &gt;60 (increased DER severity risk)</li>
</ul>
<p><strong>Drug interactions (important):</strong></p>
<table>
<tr><th>Drug</th><th>Interaction</th></tr>
<tr><td>Metronidazole</td><td>Psychosis and confusion — absolute contraindication</td></tr>
<tr><td>Warfarin</td><td>Increases INR — monitor closely, reduce warfarin dose</td></tr>
<tr><td>Phenytoin</td><td>Increases phenytoin levels — toxicity risk</td></tr>
<tr><td>Isoniazid (INH)</td><td>Neuropsychiatric effects</td></tr>
<tr><td>Benzodiazepines</td><td>Increases diazepam and chlordiazepoxide levels</td></tr>
<tr><td>Tricyclic antidepressants</td><td>Increased serum levels</td></tr>
</table>
<p><strong>Hidden alcohol sources:</strong> DER can be triggered by alcohol in mouthwash, aftershave, perfume, some cough syrups, cooking wine, and hand sanitiser (used near mouth). Counsel patients specifically.</p>
<p><strong>Supervised administration:</strong> Disulfiram's effectiveness is substantially improved when a partner, family member, or pharmacist observes medication ingestion. Unsupervised disulfiram has poor real-world adherence — patients simply stop taking it before drinking. Supervised administration converts it from a willpower tool to an external control mechanism. This is the clinical reason for its use.</p>
<p><strong>Monitoring:</strong> LFTs at baseline, 2 weeks, 4 weeks, then monthly × 6 months. Hepatotoxicity (usually reversible) occurs in approximately 1–2% — stop if significant LFT elevation. Peripheral neuropathy can develop with long-term use.</p>
<p><strong>Patient selection:</strong> Best suited for highly motivated patients with good social support, strong external accountability (employment, custody, legal), and no cardiovascular or psychiatric contraindications. Not suitable as first-line without careful discussion of risks.</p>"""
            },
            {
                "id": "med_baclofen",
                "title": "Baclofen (off-label) — GABA-B agonist",
                "body": """<p><strong>Class:</strong> GABA-B receptor agonist. <strong>TGA approval:</strong> Spasticity only — off-label for AUD. <strong>PBS:</strong> Listed for spasticity; off-label for AUD (must be prescribed as private or under spasticity indication if applicable). <strong>Cost:</strong> Inexpensive — generic baclofen is low-cost.</p>
<p><strong>Mechanism:</strong> Baclofen is a selective GABA-B receptor agonist. GABA-B receptors in the ventral tegmental area (VTA) and nucleus accumbens act as autoreceptors on dopaminergic neurons — activating them reduces dopamine release in response to alcohol cues and consumption. The clinical effect is reduction in craving and, at sufficient doses, a qualitative change often described as "indifference" to alcohol — neither wanting to drink nor finding the idea distressing. This is distinct from the mechanisms of naltrexone or acamprosate.</p>
<p><strong>Evidence base:</strong></p>
<ul>
<li><strong>Ameisen (2004):</strong> A French cardiologist (himself with severe AUD) self-experimented with escalating doses of baclofen up to 270mg/day and achieved complete absence of craving and desire to drink. Published in <em>Alcohol and Alcoholism</em> — the paper that catalysed subsequent research.</li>
<li><strong>ALPADIR trial (2015, France):</strong> RCT, n=320, high-dose baclofen (180mg/day) vs placebo. Continuous abstinence rate significantly better with baclofen (57% vs 36% at 12 weeks in abstinence-goal group).</li>
<li><strong>BacALD trial (2018, Australia):</strong> RCT demonstrating benefit at 30mg/day — the lower end of doses studied. Published in <em>Drug and Alcohol Dependence</em>.</li>
<li><strong>COCHRANE (2018):</strong> Concluded baclofen probably reduces alcohol consumption but noted heterogeneity in dose protocols and outcomes across trials.</li>
<li><strong>French guidelines:</strong> Baclofen is licensed in France for AUD (2014) at doses up to 300mg/day under specific prescribing conditions — the only country with formal regulatory approval for this indication.</li>
</ul>
<p><strong>Titration protocol (standard):</strong></p>
<table>
<tr><th>Period</th><th>Daily dose</th><th>Notes</th></tr>
<tr><td>Starting dose</td><td>5–10mg TID (15–30mg/day)</td><td>With meals to reduce nausea; some start at 5mg BD</td></tr>
<tr><td>Titration rate</td><td>Increase by 10mg/day every 3–7 days</td><td>Slower titration = better tolerability</td></tr>
<tr><td>Typical therapeutic range</td><td>30–80mg/day</td><td>Most patients respond in this range</td></tr>
<tr><td>Extended range</td><td>80–180mg/day</td><td>Some patients require higher doses; use with caution and more frequent review</td></tr>
<tr><td>High-dose protocol</td><td>180–300mg/day</td><td>French protocol; specialist use; careful monitoring essential</td></tr>
</table>
<p><strong>⚠️ Critical: Withdrawal risk at high doses</strong></p>
<p>Baclofen withdrawal at high doses (typically &gt;80mg/day) can cause seizures, hallucinations, hyperthermia, and autonomic instability — a picture resembling alcohol withdrawal but potentially more severe. <strong>Never stop baclofen abruptly at high doses.</strong> Taper slowly: reduce by maximum 10mg per week. If the patient stops abruptly, treat as a medical emergency. Document this risk clearly in the patient record and ensure the patient and their significant other understand it.</p>
<p><strong>Side effects:</strong></p>
<ul>
<li><strong>Sedation:</strong> Most common and often dose-limiting; typically worse in the first 2–4 weeks and on dose increases; warn patients not to drive until stable on a dose; alcohol is profoundly additive for sedation</li>
<li>Dizziness and ataxia (dose-related)</li>
<li>Nausea (take with food)</li>
<li>Muscle weakness</li>
<li>Cognitive blunting at high doses</li>
<li>Confusion (particularly in elderly)</li>
<li>Mood changes — can worsen or improve depression depending on individual</li>
<li>Mild euphoria at higher doses (abuse potential is lower than alcohol but exists)</li>
</ul>
<p><strong>Renal dosing — important:</strong> Baclofen is predominantly renally excreted. eGFR 30–60: halve the dose. eGFR &lt;30: use very low doses (5–10mg/day) with extreme caution or avoid. Accumulation in renal impairment can cause severe central nervous system depression.</p>
<p><strong>Who benefits most:</strong> Patients with comorbid anxiety (baclofen has anxiolytic properties); severe cravings not responding to naltrexone/acamprosate; hepatic impairment (no liver metabolism); patients who describe wanting to feel "indifferent" rather than "blocked." Also used as an off-label adjunct in alcohol withdrawal in inpatient settings.</p>
<p><strong>Informed consent:</strong> Document the off-label nature, evidence base, titration plan, and withdrawal risk in the medical record. Consider a specific consent discussion.</p>"""
            },
            {
                "id": "med_gabapentin",
                "title": "Gabapentin (off-label) — withdrawal and craving",
                "body": """<p><strong>Class:</strong> α2δ calcium channel subunit ligand (gabapentinoid). <strong>TGA approval:</strong> Epilepsy, neuropathic pain. <strong>PBS:</strong> Listed for epilepsy and neuropathic pain — off-label for AUD. <strong>Brand:</strong> Neurontin; generic gabapentin widely available and inexpensive.</p>
<p><strong>Mechanism:</strong> Binds to the α2δ subunit of voltage-gated calcium channels in presynaptic neurons, reducing release of excitatory neurotransmitters (glutamate, noradrenaline). Effectively reduces neuronal hyperexcitability — the same excitatory rebound that drives withdrawal symptoms and protracted craving. Also has significant anxiolytic and sleep-promoting effects through these mechanisms.</p>
<p><strong>Uses in AUD:</strong></p>
<ul>
<li><strong>Acute alcohol withdrawal (mild–moderate):</strong> An alternative or adjunct to benzodiazepines with growing evidence. Advantages: no misuse potential compared to benzodiazepines; no synergistic respiratory depression with residual alcohol; effective for insomnia and anxiety component. Commonly used in patients where benzodiazepine use is a concern.</li>
<li><strong>Protracted abstinence syndrome:</strong> The anxiety, insomnia, dysphoria, and craving that persist weeks to months after cessation. Gabapentin addresses these directly through its GABAergic and sleep-promoting effects.</li>
<li><strong>Craving reduction:</strong> Evidence from Mason et al (JAMA Internal Medicine, 2014): gabapentin 900mg or 1800mg/day vs placebo — dose-dependent reduction in heavy drinking days and improvement in insomnia and mood.</li>
</ul>
<p><strong>Dosing:</strong></p>
<table>
<tr><th>Indication</th><th>Dose</th><th>Notes</th></tr>
<tr><td>Acute withdrawal (inpatient/supervised)</td><td>400mg Q6H on day 1, taper over 5–7 days</td><td>In addition to or instead of benzodiazepines in mild withdrawal</td></tr>
<tr><td>Protracted withdrawal / craving</td><td>300mg TID, increasing to 600–900mg TID</td><td>Take largest dose at night (sleep benefit)</td></tr>
<tr><td>Target maintenance</td><td>900–1800mg/day in divided doses</td><td>Higher doses in Mason trial showed better outcomes</td></tr>
<tr><td>Maximum</td><td>3600mg/day (clinical trials)</td><td>Higher doses not typically needed in AUD</td></tr>
</table>
<p><strong>Renal dosing — significant adjustment required:</strong></p>
<table>
<tr><th>eGFR (mL/min)</th><th>Dose adjustment</th></tr>
<tr><td>&gt;60</td><td>Standard dosing</td></tr>
<tr><td>30–60</td><td>Reduce total daily dose by 50%</td></tr>
<tr><td>15–30</td><td>Reduce total daily dose by 75%</td></tr>
<tr><td>&lt;15 or dialysis</td><td>Specialist guidance; very low doses only</td></tr>
</table>
<p><strong>Side effects:</strong> Sedation (common, dose-related, useful at night); dizziness and ataxia; peripheral oedema; weight gain with chronic use; cognitive blunting; mood changes.</p>
<p><strong>Misuse potential:</strong> Gabapentinoids (gabapentin and pregabalin) have established misuse potential, particularly in people with co-occurring opioid use disorder where rates of misuse are high. In AUD as the primary presentation without opioid use history, misuse risk is lower but not absent. Consider this in patients with a pattern of multiple substance dependencies. Monitor for dose escalation beyond prescribed amounts.</p>
<p><strong>Drug interactions:</strong> Opioids (additive CNS and respiratory depression — important in pain management context); other CNS depressants including alcohol (do not combine with active heavy drinking); morphine increases gabapentin levels by ~44%.</p>
<p><strong>Discontinuation:</strong> Taper gradually after extended use — abrupt cessation at high doses can cause anxiety, insomnia, and nausea; seizures reported rarely.</p>"""
            },
            {
                "id": "med_topiramate",
                "title": "Topiramate (off-label) — slow titration required",
                "body": """<p><strong>Class:</strong> Anticonvulsant with multiple mechanisms. <strong>TGA approval:</strong> Epilepsy, migraine prophylaxis. <strong>PBS:</strong> Listed for epilepsy and migraine — off-label for AUD. <strong>Brand:</strong> Topamax; generics available.</p>
<p><strong>Mechanism (multiple):</strong> Enhances GABA-A activity; antagonises AMPA/kainate glutamate receptors; blocks voltage-gated sodium and calcium channels; inhibits carbonic anhydrase. The net effect on the reward circuitry is complex but results in significant reduction in the urge to drink and pleasurable effects of alcohol.</p>
<p><strong>Evidence:</strong> Johnson et al (JAMA, 2007): topiramate 300mg/day vs placebo — significantly greater reductions in heavy drinking days, drinks per day, and drinks per drinking day. A subsequent Cochrane review (2010) confirmed the evidence base. Particularly strong for reducing heavy drinking days rather than maintaining abstinence — complementary to acamprosate's abstinence-maintenance effect.</p>
<p><strong>Titration — this is critical; rushing causes intolerable side effects:</strong></p>
<table>
<tr><th>Weeks</th><th>Morning dose</th><th>Evening dose</th><th>Total/day</th></tr>
<tr><td>1–2</td><td>—</td><td>25mg</td><td>25mg</td></tr>
<tr><td>3–4</td><td>25mg</td><td>25mg</td><td>50mg</td></tr>
<tr><td>5–6</td><td>25mg</td><td>50mg</td><td>75mg</td></tr>
<tr><td>7–8</td><td>50mg</td><td>50mg</td><td>100mg</td></tr>
<tr><td>9–10</td><td>50mg</td><td>75mg</td><td>125mg</td></tr>
<tr><td>11–12</td><td>75mg</td><td>75mg</td><td>150mg</td></tr>
<tr><td>Onwards to target</td><td>Continue increasing by 25mg/week</td><td></td><td>Target 200–300mg/day</td></tr>
</table>
<p><strong>Side effects — important to counsel specifically:</strong></p>
<ul>
<li><strong>Paresthesias</strong> (tingling, particularly hands, feet, face): nearly universal at initiation — not dangerous, typically resolves in 2–6 weeks; warn patients explicitly so they are not alarmed</li>
<li><strong>Cognitive slowing / "dopamax":</strong> Word-finding difficulties, psychomotor slowing, memory impairment — dose-dependent; most patients adapt; more pronounced at higher doses and rapid titration; if severe, reduce dose or accept lower target</li>
<li><strong>Weight loss:</strong> Consistent and can be clinically significant (2–5kg typical) — often acceptable or desirable in AUD patients who are overweight; combination with GLP-1 agents may be additive</li>
<li><strong>Kidney stones:</strong> Carbonic anhydrase inhibition reduces urinary citrate; risk approximately 1.5% per year of use; advise adequate hydration (≥2L/day); potassium citrate supplementation may be used preventively in high-risk patients</li>
<li><strong>Metabolic acidosis:</strong> Carbonic anhydrase inhibition reduces bicarbonate; monitor serum bicarbonate; usually mild but can affect bone health and growth in children</li>
<li><strong>Mood changes:</strong> Depression and irritability reported; monitor; occasionally psychosis at high doses</li>
<li><strong>Acute glaucoma:</strong> Rare but genuine emergency — acute angle-closure glaucoma with eye pain and vision change; discontinue immediately and refer urgently</li>
</ul>
<p><strong>Contraindications:</strong> Pregnancy (teratogenic — cleft palate, hypospadias; ensure effective contraception and counsel); nephrolithiasis history (relative — not absolute but increases risk further); severe hepatic impairment.</p>
<p><strong>Monitoring:</strong> Serum bicarbonate at baseline and every 3 months; renal function; cognitive function assessment; weight. Consider eye check if glaucoma symptoms.</p>
<p><strong>Practical note:</strong> Topiramate has a higher side effect burden than naltrexone or acamprosate but offers genuine benefits for patients who have not responded to first-line options, and the weight loss effect is often advantageous. The cognitive side effects are the main limiting factor — going slowly on titration is the single most important factor for tolerability.</p>"""
            },
            {
                "id": "med_glp1",
                "title": "GLP-1 receptor agonists — semaglutide and liraglutide (emerging evidence)",
                "body": """<p><strong>Class:</strong> Glucagon-like peptide-1 (GLP-1) receptor agonists. <strong>TGA-approved indications:</strong> Type 2 diabetes mellitus; obesity (BMI ≥30, or ≥27 with weight-related comorbidity). <strong>AUD indication:</strong> Off-label; not approved. <strong>PBS:</strong> Listed for T2DM and obesity — prescribable for AUD patients who also meet these criteria.</p>
<p><strong>Agents:</strong></p>
<table>
<tr><th>Agent</th><th>Brand(s)</th><th>Route</th><th>Frequency</th></tr>
<tr><td>Semaglutide</td><td>Ozempic (diabetes), Wegovy (obesity)</td><td>Subcutaneous injection</td><td>Weekly</td></tr>
<tr><td>Oral semaglutide</td><td>Rybelsus</td><td>Oral tablet</td><td>Daily (fasting)</td></tr>
<tr><td>Liraglutide</td><td>Victoza (diabetes), Saxenda (obesity)</td><td>Subcutaneous injection</td><td>Daily</td></tr>
<tr><td>Exenatide</td><td>Byetta, Bydureon</td><td>SC injection</td><td>BD or weekly (ER)</td></tr>
</table>
<p><strong>Mechanism in AUD:</strong> GLP-1 receptors are expressed throughout the mesolimbic dopamine system — specifically the VTA and nucleus accumbens. Preclinical and emerging clinical evidence suggests GLP-1 receptor activation reduces dopamine release in response to alcohol cues, reduces the rewarding properties of alcohol, reduces impulsivity, and improves prefrontal inhibitory control. The mechanism is distinct from all other approved AUD medications.</p>
<p><strong>Standard dosing (semaglutide SC — most evidence):</strong></p>
<table>
<tr><th>Period</th><th>Dose</th><th>Notes</th></tr>
<tr><td>Weeks 1–4</td><td>0.25mg SC weekly</td><td>Starting dose — not therapeutic for weight/diabetes; titration only</td></tr>
<tr><td>Weeks 5–8</td><td>0.5mg SC weekly</td><td>First maintenance dose</td></tr>
<tr><td>Weeks 9–12</td><td>1mg SC weekly</td><td>Standard effective dose</td></tr>
<tr><td>Onwards (if needed)</td><td>2mg SC weekly</td><td>Maximum approved dose; higher doses in trials</td></tr>
</table>
<p><strong>Current evidence base for AUD:</strong></p>
<ul>
<li><strong>Preclinical (animal models):</strong> Robust, consistent reduction in alcohol self-administration across multiple rodent and primate models for multiple GLP-1 agonists</li>
<li><strong>Klausen et al (2022, Biological Psychiatry):</strong> Semaglutide significantly reduced alcohol consumption in a rat model of AUD; effects comparable to established medications</li>
<li><strong>Danish register study (Becker et al, 2024):</strong> Population-level observational data showing patients with AUD on GLP-1 agonists (for diabetes/obesity) had significantly lower rates of AUD-related hospitalisation over 12 months</li>
<li><strong>Clinical anecdote:</strong> Large numbers of patients on semaglutide for obesity/diabetes are spontaneously reporting dramatic reductions in alcohol desire — appearing widely in patient forums, medical social media, and clinician observations globally</li>
<li><strong>RCTs:</strong> Multiple trials currently underway (NIAAA-funded; European investigator-initiated). Results expected 2025–2027.</li>
<li><strong>Leggio et al (2023, Cell Metabolism):</strong> Comprehensive review concluding GLP-1 system is a promising therapeutic target for AUD and other addictions</li>
</ul>
<p><strong>Contraindications:</strong></p>
<ul>
<li><strong>Absolute:</strong> Personal or family history of medullary thyroid carcinoma; Multiple Endocrine Neoplasia type 2 (MEN2)</li>
<li><strong>Relative:</strong> History of pancreatitis (risk of recurrence); severe gastroparesis; severe renal impairment (limited data); active eating disorder where further appetite suppression is contraindicated</li>
</ul>
<p><strong>Side effects:</strong> Nausea (most common — typically front-loaded, improves after 4–8 weeks; manage by slow titration and advising smaller meals); vomiting; diarrhoea or constipation; decreased appetite; pancreatitis (rare — stop immediately if persistent upper abdominal pain); gallstone formation with rapid weight loss; injection site reactions; mild tachycardia.</p>
<p><strong>Clinical considerations for AUD:</strong> The PBS listing for obesity (BMI ≥30, or ≥27 with comorbidity) and T2DM means that many patients with AUD who are overweight or diabetic can access these medications at PBS cost. For the subset where AUD is the only indication, cost is the primary barrier (Ozempic approximately $150–400/month privately).</p>
<p><strong>Bottom line:</strong> GLP-1 agonists represent a potentially transformative development in AUD pharmacotherapy — targeting the reward circuitry through a mechanism entirely distinct from existing medications. The preclinical and emerging clinical data are compelling. This is the medication to watch, and it is already clinically deployable in patients who meet the existing PBS criteria for diabetes or obesity.</p>"""
            }
        ]
    },
    {
        "label": "Recovery and Support",
        "optional": True,
        "items": [
            {
                "id": "aud_cravings",
                "title": "Managing cravings and high-risk situations",
                "body": """<p><strong>Understanding cravings:</strong> Cravings are automatic neurological responses — not moral failures or signs of inadequate motivation. They are triggered by conditioned cues (places, times, emotions, social contexts) and involve activation of the same brain circuits that processed the original reward. They are time-limited: most cravings peak within 15–30 minutes and resolve regardless of whether drinking occurs.</p>
<p><strong>Urge surfing:</strong> A mindfulness-based technique for riding out craving without acting on it. The metaphor: a craving is a wave — it builds, peaks, and passes. The goal is to observe the craving without fusing with it: notice the physical sensations (tension, restlessness, salivation), observe them without judgment, allow them to peak and subside. Does not require suppression or resistance — only observation and tolerance of discomfort.</p>
<p><strong>HALT — common craving triggers:</strong></p>
<ul>
<li><strong>H</strong>ungry — blood sugar drops increase craving and reduce impulse control. Eat regularly.</li>
<li><strong>A</strong>ngry — negative emotions are one of the strongest relapse triggers. Have a plan for managing anger that does not involve drinking.</li>
<li><strong>L</strong>onely — social isolation is a major trigger and consequence of AUD. Identify people to contact.</li>
<li><strong>T</strong>ired — fatigue impairs prefrontal function (decision-making, impulse control) — the same circuitry alcohol has already damaged. Sleep matters.</li>
</ul>
<p><strong>Relapse prevention planning:</strong> A written plan identifying: personal high-risk situations; early warning signs specific to the individual; specific coping strategies for each trigger; who to call if urges become strong; what to do in the first hour after a slip. The plan should exist before the high-risk situation, not be constructed during it.</p>
<p><strong>Managing a slip:</strong> A slip (single episode of drinking after a period of abstinence or controlled drinking) is not the same as a full relapse. The "abstinence violation effect" — the shame and catastrophising that follows a slip and often drives continued drinking ("I've ruined it, I might as well keep going") — is predictable and addressable. The appropriate response to a slip is immediate re-engagement with treatment, not escalation.</p>"""
            },
            {
                "id": "aud_sleep",
                "title": "Sleep and alcohol",
                "body": """<p><strong>How alcohol disrupts sleep:</strong> Alcohol is not a sleep aid — it is a sedative with profoundly disruptive effects on sleep architecture:</p>
<ul>
<li><strong>REM suppression:</strong> Alcohol suppresses rapid eye movement (REM) sleep in the first half of the night. REM sleep is critical for emotional memory processing, consolidation of new learning, and psychological restoration. Chronic REM suppression is associated with worsening mood and cognitive function.</li>
<li><strong>Sleep fragmentation:</strong> As alcohol is metabolised in the second half of the night, there is a rebound in arousal — frequent awakening, light sleep, early morning waking. Net sleep quality is significantly worse despite feeling sedated to sleep.</li>
<li><strong>Rebound insomnia:</strong> After stopping alcohol, severe insomnia is near-universal for the first 1–4 weeks. The brain's hyperexcitable state (withdrawal) directly interferes with sleep initiation and maintenance. This is one of the most powerful relapse triggers — people return to drinking specifically because they cannot sleep without it.</li>
</ul>
<p><strong>Sleep improvement with abstinence:</strong> Sleep typically begins to improve after 2–6 weeks of abstinence. Full normalisation of sleep architecture may take several months. Inform patients of this timeline to prevent the misconception that abstinence will immediately solve their sleep problems.</p>
<p><strong>Managing withdrawal-related insomnia without new dependence:</strong></p>
<ul>
<li>Gabapentin has good evidence for improving sleep in early abstinence through its GABA-ergic effects (see Medications)</li>
<li>Trazodone 50–100mg nocte is commonly used — minimal dependence risk</li>
<li>Mirtazapine has sedating properties and may also address co-occurring depressive symptoms</li>
<li>Melatonin (2mg prolonged-release) can help with sleep initiation</li>
<li><strong>Avoid benzodiazepines and Z-drugs for insomnia in AUD</strong> — high dependence risk and cross-tolerance with alcohol makes these particularly problematic</li>
</ul>
<p><strong>CBT for Insomnia (CBT-I):</strong> The most effective long-term treatment for insomnia. Includes sleep restriction therapy, stimulus control, sleep hygiene, and addressing maladaptive sleep beliefs. Evidence is strong. Digital CBT-I programmes (Sleepio, SHUTi) and the UNSW-developed app are available when therapist access is limited. Refer to our insomnia psychoeducation handout for detail.</p>"""
            },
            {
                "id": "aud_relationships",
                "title": "Relationships, family, and carers",
                "body": """<p><strong>The impact on relationships:</strong> AUD profoundly affects intimate relationships, parenting, friendships, and work relationships. Unreliability, mood dysregulation during intoxication or withdrawal, secrecy, financial impact, and the emotional unavailability of chronic intoxication all erode trust over time. Partners and family members commonly experience a range of responses that may look like codependency, enabling, or hypervigilance — these are normal adaptive responses to living with unpredictability and are not character flaws.</p>
<p><strong>Enabling vs supporting:</strong> These are easily confused. Enabling — protecting the person with AUD from the consequences of their drinking (covering for absences, managing the DUI, calling in sick on their behalf) — inadvertently reduces motivation to change by removing natural consequences. Supporting — being present without judgement, encouraging treatment engagement, maintaining the relationship — is different. The boundary is not always obvious and family members benefit from specific guidance.</p>
<p><strong>Al-Anon:</strong> A 12-step mutual support programme specifically for family members and friends of people with AUD. Focuses on the family member's own wellbeing, detachment from the drinker's behaviour, and breaking enabling patterns. Widely available, free, and no professional referral required. <a href="https://al-anon.org.au" target="_blank">al-anon.org.au</a></p>
<p><strong>CRAFT (Community Reinforcement and Family Training):</strong> An evidence-based approach for family members wanting to help someone who is not yet treatment-engaged. Unlike confrontational approaches (family interventions, Tough Love), CRAFT has strong evidence for actually getting the person with AUD into treatment. Focuses on communication skills, positive reinforcement of non-drinking behaviour, allowing natural consequences, and the carer's own wellbeing. Available through SMART Recovery and trained AOD counsellors.</p>
<p><strong>Children in the household:</strong> Children of parents with AUD are at significantly elevated risk for their own AUD (genetic and environmental), anxiety and depression, developmental difficulties, and adverse childhood experiences. Brief intervention and referral to child-specific services (Family Drug Support, school counsellors) is an important part of holistic care.</p>
<p><strong>Stigma:</strong> Stigma about AUD is pervasive and harmful — in healthcare settings, workplaces, and communities. Patients commonly delay seeking help for years because of shame. Naming stigma directly and normalising help-seeking is a clinical task, not an optional extra. Your response to the patient discussing alcohol determines whether they will return.</p>"""
            },
            {
                "id": "aud_resources",
                "title": "Support services and resources (Australia)",
                "body": """<p><strong>DirectLine — 1800 888 236</strong><br>Free, confidential 24/7 telephone counselling for alcohol and drug concerns. Available to individuals and family members. Can provide referral to local treatment services. No appointment required.</p>
<p><strong>Alcohol and Drug Foundation</strong><br>National Australian organisation providing evidence-based information about alcohol and other drugs, helpline support, service directory, and community programmes. <a href="https://adf.org.au" target="_blank">adf.org.au</a></p>
<p><strong>Hello Sunday Morning / Daybreak app</strong><br>Australia's largest digital alcohol behaviour change platform. The Daybreak app provides peer support, tracking, and structured behaviour change programmes specifically for alcohol. Free. Evidence-based. Particularly useful for people not ready for formal treatment or as an adjunct. <a href="https://hellosundaymorning.org" target="_blank">hellosundaymorning.org</a></p>
<p><strong>SMART Recovery Australia</strong><br>Free, evidence-based (CBT) mutual support meetings as an alternative or complement to AA. Face-to-face meetings, online meetings. No 12-step or spiritual framework required. <a href="https://www.smartrecovery.org.au" target="_blank">smartrecovery.org.au</a></p>
<p><strong>Alcoholics Anonymous (AA)</strong><br>Widely available mutual support programme; 12-step spiritual framework; largest peer support network in the world for AUD. Local meetings at <a href="https://www.aa.org.au" target="_blank">aa.org.au</a></p>
<p><strong>Family Drug Support — 1300 368 186</strong><br>Support specifically for families and carers of people with alcohol and drug problems. Available 24/7. Also offers CRAFT-aligned educational workshops.</p>
<p><strong>Turning Point</strong><br>Victorian AOD research and clinical service. Online screening, self-help resources, and clinical service access. Also produces the comprehensive Alcohol and Drug Foundation Drug Index. <a href="https://www.turningpoint.org.au" target="_blank">turningpoint.org.au</a></p>
<p><strong>NIDA (National Institute on Drug Abuse)</strong><br>US-based but extensive and freely available evidence-based resources on AUD biology, treatment, and self-help. <a href="https://nida.nih.gov" target="_blank">nida.nih.gov</a></p>
<p><strong>Lifeline — 13 11 14</strong><br>24/7 crisis support for emotional distress and suicide. When AUD intersects with crisis, Lifeline is available around the clock.</p>
<p><strong>Beyond Blue — 1300 22 4636</strong><br>Mental health support for depression, anxiety, and related conditions that commonly co-occur with AUD. Online chat available.</p>"""
            }
        ]
    }
]

def build_items_js(groups):
    lines = []
    lines.append("var AUD_PE_GROUPS=[")
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
<title>Alcohol Use Disorder Psychoeducation — Dr Benjamin Murrie</title>
<style>
:root{--bg:#f0f2f5;--surface:#fff;--border:#e2e6ed;--text:#1a1d23;--muted:#6b7280;--aud:#15803d;--aud-bg:#dcfce7;--aud-dark:#14532d;--aud-mid:#166534;--navy:#0f172a;--sans:-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--text);font-size:15px;min-height:100vh}
.topbar{background:var(--navy);padding:10px 14px;border-bottom:3px solid var(--aud);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.topbar-title{font-size:13px;font-weight:800;color:#bbf7d0;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ti{background:#1e293b;border:1px solid #334155;color:#f1f5f9;padding:5px 9px;border-radius:7px;font:inherit;font-size:13px;min-width:0}
.ti::placeholder{color:#64748b}
.ti:focus{outline:1px solid var(--aud);background:#243349}
.content{max-width:1000px;margin:0 auto;padding:14px 12px 40px}
.condition-block{margin-bottom:14px;border-radius:10px;overflow:hidden;border:1px solid var(--border)}
.condition-header{padding:10px 14px;font:700 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:10px;background:var(--aud-dark)}
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
.pe-body th{background:#f0fdf4;padding:5px 8px;text-align:left;border:1px solid var(--border);font-size:11px}
.pe-body td{padding:4px 8px;border:1px solid var(--border);vertical-align:top}
.pe-body a{color:var(--aud-mid)}
.pe-section.aud-done{background:#f0fdf4}
.pe-section.aud-done .pe-tick-btn{color:var(--aud)}
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
.ho-notice{font-size:9.5pt;background:#f0fdf4;border-left:3px solid #15803d;padding:9px 12px;line-height:1.5;color:#14532d}
.ho-group-label{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:14px 0 6px;padding-bottom:3px;border-bottom:2px solid currentColor}
.ho-group-label.aud-g-core{color:#14532d;border-bottom-color:#14532d}
.ho-group-label.aud-g-treatment{color:#1e3a5f;border-bottom-color:#1e3a5f}
.ho-group-label.aud-g-medications{color:#6d28d9;border-bottom-color:#6d28d9}
.ho-group-label.aud-g-recovery{color:#0e7490;border-bottom-color:#0e7490}
.ho-topic{margin-bottom:20px;padding:11px 14px;border:1px solid #e5e7eb;border-radius:7px;background:#f9fff9}
.ho-topic-title{font-weight:700;font-size:11pt;color:#0f172a;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb}
.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151}
.ho-topic-body p{margin:0 0 6px}
.ho-topic-body p:last-child{margin:0}
.ho-topic-body ul{margin:3px 0 7px 16px}
.ho-topic-body li{margin-bottom:3px}
.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:5px 0 8px}
.ho-topic-body th{background:#f0fdf4;padding:4px 7px;text-align:left;border:1px solid #d1d5db;font-size:9pt}
.ho-topic-body td{padding:3pt 7pt;border:1px solid #d1d5db;vertical-align:top}
.ho-topic-body a{color:#15803d}
.ho-footer{margin-top:24px;padding-top:12px;border-top:1px solid #e5e7eb;font-size:8.5pt;color:#9ca3af;font-style:italic}
</style>
</head>
<body>
<div class="topbar">
  <span class="topbar-title">Alcohol Use Disorder Psychoeducation</span>
  <input class="ti" id="ptName" placeholder="Patient name..." style="flex:1;min-width:130px;max-width:210px" oninput="refresh()">
  <input class="ti" id="ptDate" type="date" style="flex:0 0 128px" oninput="refresh()">
  <input class="ti" id="drName" placeholder="Clinician name..." style="flex:1;min-width:130px;max-width:200px" oninput="refresh()">
</div>
<div class="content">
  <div class="condition-block" style="margin-top:12px">
    <div class="condition-header">
      Alcohol Use Disorder — Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll()">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll()">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="aud-topic-list"></div>
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

var GROUP_COLOR_CLASS={'null':'aud-g-core','Treatment':'aud-g-treatment','Medications':'aud-g-medications','Recovery and Support':'aud-g-recovery'};

function renderTopics(){
  var el=$('aud-topic-list'); if(!el) return;
  var html='';
  AUD_PE_GROUPS.forEach(function(g){
    if(g.label) html+='<div class="pe-group-label">'+(g.optional?'<span style="font-size:9px;opacity:.6;font-weight:600;margin-right:4px">OPTIONAL</span>':'')+esc(g.label)+'</div>';
    g.items.forEach(function(item){
      var done=!!sel[item.id];
      html+='<div class="pe-section'+(done?' aud-done':'')+(g.optional?' pe-optional':'')+'" data-id="'+item.id+'">';
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
      sec.classList.toggle('aud-done',!!sel[id]);
      sec.querySelector('.pe-tick-btn').innerHTML=sel[id]?'&#9745;':'&#9744;';
      refresh();
    } else {
      var hdr=e.target.closest('.pe-header'); if(hdr) sec.classList.toggle('pe-open');
    }
  };
}
function selectAll(){AUD_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){sel[item.id]=true;});});renderTopics();refresh();}
function clearAll(){Object.keys(sel).forEach(function(k){sel[k]=false;});renderTopics();refresh();}

function buildHandout(){
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var hasAny=false;
  AUD_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){if(sel[item.id])hasAny=true;});});
  if(!hasAny) return null;
  var h='';
  h+='<div class="ho-header">';
  h+='<div class="ho-pt">Psychoeducation Handout — Alcohol Use Disorder</div>';
  h+='<div class="ho-meta">Patient: <strong>'+esc(name)+'</strong>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <strong>'+esc(dr)+'</strong></div>';
  h+='</div>';
  var currentGroup=null;
  AUD_PE_GROUPS.forEach(function(g){
    g.items.forEach(function(item){
      if(!sel[item.id]) return;
      var gKey=g.label||'null';
      if(gKey!==currentGroup){
        if(g.label){
          var cls=GROUP_COLOR_CLASS[g.label]||'aud-g-core';
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
    '.ho-notice{font-size:9.5pt;background:#f0fdf4;border-left:3pt solid #15803d;padding:8pt 10pt;color:#14532d;}'+
    '.ho-group-label{font-size:8.5pt;font-weight:bold;text-transform:uppercase;letter-spacing:.06em;margin:11pt 0 5pt;padding-bottom:2pt;border-bottom:1.5pt solid currentColor;}'+
    '.ho-group-label.aud-g-core{color:#14532d;}.ho-group-label.aud-g-treatment{color:#1e3a5f;}.ho-group-label.aud-g-medications{color:#6d28d9;}.ho-group-label.aud-g-recovery{color:#0e7490;}'+
    '.ho-topic{margin-bottom:20pt;padding:10pt 13pt;border:1pt solid #e5e7eb;background:#f9fff9;}'+
    '.ho-topic-title{font-weight:bold;font-size:11pt;color:#0f172a;margin:0 0 5pt;padding-bottom:4pt;border-bottom:1pt solid #e5e7eb;}'+
    '.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151;}'+
    '.ho-topic-body p{margin:0 0 5pt;}.ho-topic-body ul{margin:3pt 0 6pt 14pt;}.ho-topic-body li{margin-bottom:3pt;}'+
    '.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9pt;margin:5pt 0 8pt;}'+
    '.ho-topic-body th{background:#f0fdf4;padding:4pt 6pt;text-align:left;border:1pt solid #d1d5db;font-size:8.5pt;}'+
    '.ho-topic-body td{padding:3pt 6pt;border:1pt solid #d1d5db;vertical-align:top;}'+
    '.ho-footer{margin-top:20pt;padding-top:10pt;border-top:1pt solid #e5e7eb;font-size:8pt;color:#9ca3af;font-style:italic;}'+
    '</style></head><body>'+html+'</body></html>';
}

function dlDocx(){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected.');return;}
  var name=(f('ptName')||'Patient').replace(/[^a-zA-Z0-9]/g,'_');
  var blob=new Blob(['﻿'+docx],{type:'application/msword;charset=utf-8'});
  var url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='AUD_Psychoeducation_'+name+'.doc';
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
out = os.path.join(BASE, 'aud-psychoeducation.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print("Done.")
