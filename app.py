import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
# loading the saved models

diabetes_model = pickle.load(open("./models/diabetes_model_new.sav",'rb'))
heart_model = pickle.load(open("./models/heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav",'rb'))


# sidebar navigation
with st.sidebar:

        selected = option_menu('Multiple Disease Prediction System',
                               ['Diabetes Prediction',
                                'Parkinson\'s Prediction',
                                'Heart Disease Prediction',
                                  'PARKICARE','HEALTHY HEART','DIABETES WELLNESS'],
                               icons=['heart', 'activity', 'person'],
                               default_index=0)



if(selected=='HEALTHY HEART'):
    st.title('HEALTHY HEART')
    st.markdown('---')
    st.header(" Your Personalized Guide to a Healthy Heart")
    st.write('You can do a lot to prevent or delay heart disease. You can start by changing what you eat and getting more physical activity.Avoiding tobacco products and limiting alcohol helps, too Making small changes to your daily life can add up, giving you a healthier heart.Talk with your healthcare provider about a plan that works for you.Talk with your healthcare provider about a plan that works for you.')
    st.header("Eat a healthy, balanced diet")
    st.write('A low-fat, high-fibre diet is recommended, which should include plenty of fresh fruit and vegetables (5 portions a day) and whole grains.')
    st.write('You should limit the amount of salt you eat to no more than 6g (0.2oz) a day as too much salt will increase your blood pressure. 6g of salt is about 1 teaspoonful.')
    st.write('There are 2 types of fat: saturated and unsaturated. You should avoid food containing saturated fats, because these will increase the levels of bad cholesterol in your blood.')
    st.subheader('Foods high in saturated fat include:')
    st.markdown("- meat pies")
    st.markdown("- sausages and fatty cuts of meat")
    st.markdown("- ghee – a type of butter often used in Indian cooking")
    st.markdown("- lard")
    st.markdown("- cream")
    st.markdown("- foods that contain coconut or palm oil")
    st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
            ''', unsafe_allow_html=True)

    st.write('However, a balanced diet should still include unsaturated fats, which have been shown to increase levels of good cholesterol and help reduce any blockage in your arteries.')
    st.subheader('Foods high in unsaturated fat include:')
    st.markdown("- oily fish")
    st.markdown("- avocados")
    st.markdown("- nuts and seeds")
    st.markdown("- sunflower, rapeseed, olive and vegetable oils")
    st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

    st.write('You should also try to avoid too much sugar in your diet, as this can increase your chances of developing diabetes, which is proven to significantly increase your chances of developing CHD.')
    st.subheader('Read more about:')
    st.markdown("[healthy eating](https://www.nhs.uk/live-well/eat-well/)")
    st.header("Be more physically active")
    st.markdown("- Combining a healthy diet with regular exercise is the best way of maintaining a healthy weight. Having a healthy weight reduces your chances of developing high blood pressure.")
    st.markdown("- Regular exercise will make your heart and blood circulatory system more efficient, lower your cholesterol level, and also keep your blood pressure at a healthy level.")
    st.markdown("- Exercising regularly reduces your risk of having a heart attack. The heart is a muscle and, like any other muscle, benefits from exercise. A strong heart can pump more blood around your body with less effort.")
    st.markdown("- Any aerobic exercise, such as walking, swimming and dancing, makes your heart work harder and keeps it healthy.")
    st.markdown('''
                        <style>
                        [data-testid="stMarkdownContainer"] ul{
                            padding-left:40px;
                        }
                        </style>
                        ''', unsafe_allow_html=True)
    st.subheader('Read more about:')
    st.markdown("[fitness exercise](https://www.nhs.uk/live-well/exercise/)")

    st.header("Be more physically active")
    st.write('A GP or practice nurse can tell you what your ideal weight is in relation to your height and build. Alternatively, you can' )
    st.markdown("[Calculate your body mass index (BMI)](https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/)")
    st.subheader('Read more about:')
    st.markdown("[Better Health-loss weight](https://www.nhs.uk/better-health/lose-weight/)")

    st.header("Give up smoking")
    st.text('Ask a doctor about this or visit  ')
    st.markdown("- If you smoke, giving up will reduce your risk of developing CHD.")
    st.markdown("- Smoking is a major risk factor for developing atherosclerosis (furring of the arteries).")
    st.markdown("- Research has shown you are 3 times more likely to successfully give up smoking if you use NHS support together with stop-smoking medicines, such as patches or gum.")
    st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left:40px;
                }
                </style>
                ''', unsafe_allow_html=True)
    st.markdown("[Better Health-Quit Smoking](https://www.nhs.uk/better-health/quit-smoking/)")

    st.header("Reduce your alcohol consumption")
    st.write("If you drink, do not exceed the maximum recommended limits.")
    st.markdown("- Men and women are advised not to regularly drink more than 14 units a week")
    st.markdown("- spread your drinking over 3 days or more if you drink as much as 14 units a week")
    st.markdown("- If you want to cut down, try to have several drink-free days each week")
    st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
            ''', unsafe_allow_html=True)
    st.subheader('Read more about:')
    st.markdown("[alcohol-advice](https://www.nhs.uk/live-well/alcohol-advice/)")

    st.header("Keep your blood pressure under control")
    st.write('You can keep your blood pressure under control by eating a healthy diet low in saturated fat, exercising regularly and, if needed, taking medicine to lower your blood pressure.')
    st.write('Your target blood pressure should be below 135/85mmHg. If you have high blood pressure, ask a GP to check your blood pressure regularly.')
    st.subheader('Read more about:')
    st.markdown("[high-blood-pressure](https://www.nhs.uk/conditions/high-blood-pressure-hypertension/)")


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction ')
    img = Image.open('diab.jpg')
    st.image(img)


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for prediction
    diab_diagnosis = ''

    # create a button for prediction

    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.warning("Please fill in all the fields.")
        else:
            diab_prediction = diabetes_model.predict(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)



if(selected=='DIABETES WELLNESS'):
    st.title('DIABETES WELLNESS')
    st.markdown('---')
    st.header("The Diabetes Wellness Companion: A Guide to Health and Vitality")
    st.subheader("Diabetes is a condition that causes a person's blood sugar level to become too high.")
    st.text('There are 2 main types of diabetes:')

    st.markdown("[type 1 diabetes](https://www.nhs.uk/conditions/type-1-diabetes/)")
    st.write("a lifelong condition where the body's immune system attacks and destroys the cells that produce insulin")
    st.markdown("[type 2 diabetes](https://www.nhs.uk/conditions/type-2-diabetes/)")
    st.write("where the body does not produce enough insulin, or the body's cells do not react to insulin properly")
    st.text('Type 2 diabetes is far more common than type 1')
    st.write('High blood sugar that develops during pregnancy is known as gestational diabetes. It usually goes away after giving birth.')
    st.write('Many people have blood sugar levels above the normal range, but not high enough to be diagnosed as having diabetes. This is known as non-diabetic hyperglycaemia, or pre-diabetes.')
    st.write('People with non-diabetic hyperglycaemia are at greater risk of developing type 2 diabetes, but the risk can be reduced through lifestyle changes.')

    st.subheader('Healthy Weight')
    st.write('You may not get down to the number you saw on the scale 20 years ago, but you can still get to a weight that enhances your health and your life.')
    st.write('First, what does “healthy weight” mean to you? Is it the weight you think you should be? The same as you weighed 20 years ago? Ten pounds less than your sister-in-law? We can’t provide an exact number for you personally, but we can give you some pointers on how to get to a weight that’s healthy for you and stay there.')
    st.subheader('Two ways to get a ballpark idea if your weight is health')
    st.markdown("[BMI](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html)")
    st.markdown("[Weight circumference](https://www.cdc.gov/healthyweight/assessing/index.html)")

    st.subheader('Eat Well')
    st.write('Managing blood sugar is the key to living well with diabetes, and eating well is the key to managing blood sugar. But what does it mean to eat well? Simply put, eat healthy foods in the right amounts at the right times so your blood sugar stays in your target range as much as possible.')
    st.markdown("[Diabetes Meal Planning](https://www.cdc.gov/diabetes/managing/eat-well/meal-plan-method.html)")
    st.markdown("[Grocery Shopping](https://www.cdc.gov/diabetes/managing/eat-well/grocery-shopping.html)")
    st.markdown("[Food Labels](https://www.cdc.gov/diabetes/managing/eat-well/food-labels.html)")
    st.markdown("[Eating Out](https://www.cdc.gov/diabetes/managing/eat-well/eating-out.html)")

    st.subheader('Get Active!')
    st.write('Being More Active Is Better for You')
    st.write('If you have diabetes, being active makes your body more sensitive to insulin (the hormone that allows cells in your body to use blood sugar for energy), which helps manage your diabetes. Physical activity also helps control blood sugar levels and lowers your risk of heart disease and nerve damage.')
    st.header("Some additional benefits include:")
    st.write("-Maintaining a healthy weight")
    st.markdown("-Losing weight, if needed")
    st.markdown("- Feeling happier")
    st.markdown("- Sleeping better")
    st.markdown("- Improving your memory")
    st.markdown("-Controlling your blood pressure")
    st.markdown("- Lowering LDL (“bad”) cholesterol and raising HDL (“good”) cholesterol")
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)
    st.markdown("[Get Active!](https://www.cdc.gov/diabetes/managing/active.html)")

    st.subheader('Find the right medications.')
    st.write('Different non-insulin drugs lower your blood sugar by different actions:')
    st.markdown("-They may encourage your pancreas to make more insulin.")
    st.markdown("- They can help your body respond better to insulin.")
    st.markdown("-They may mimic the action of a substance in your body called GLP-1, which lowers your blood sugar after meals.")
    st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
            ''', unsafe_allow_html=True)
    st.write('Your doctor may suggest that you start taking just one medication, then add more options over time if you can’t get your blood sugar under control. However, if your A1C level—a measure of your long-term blood sugar—is especially high when you’re diagnosed, your doctor may suggest that you start taking more than one medication to control your blood sugar right away.')

    st.subheader('Track your blood sugar')
    st.write(' Your doctor may want you to regularly check your blood sugar and report the results. Ask your doctor or pharmacist to recommend a blood sugar monitor that is easy for you to use. Some have backlighting and large numbers so you can see the results more easily, Kalyani says, and some store multiple readings over time so you can just download the results at your doctor’s office.')

    st.subheader('Keep your blood sugar from going too low')
    st.write('Some diabetes medications can cause your blood sugar to drop too low. This problem is called hypoglycemia, and it can be serious. Know how to recognize the symptoms of hypoglycemia (such as shakiness, sweating, and confusion) and talk to your doctor about how to treat it.')

    st.subheader('Living With...')
    st.write('“With proper self-management and good education, people with diabetes can live long, healthy lives,” Kalyani says. “If well-controlled, it should not detract from their quality of life but will require some adjustments to their daily routine.”')






# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction')
    img = Image.open('heart.jpg')
    st.image(img)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversible defect')



    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]):
            st.warning("Please fill in all the fields.")
        else:
            heart_prediction = np.array([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])

            if (heart_prediction[0] == 1):
              heart_diagnosis = 'The person has a heart disease'
            else:
              heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


if(selected=='PARKICARE'):
    st.title("PARKICARE")
    st.markdown('---')
    st.header(" Empowering Wellness Through Personalized Parkinson's Care")
    st.subheader("There's currently no cure for Parkinson's disease, but treatments are available to help relieve the symptoms and maintain your quality of life.")
    st.write('These treatments include:')
    st.markdown("- supportive therapies, such as physiotherapy")
    st.markdown("- medication")
    st.markdown( "- surgery (for some people)")
    st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left:40px;
                }
                </style>
                ''', unsafe_allow_html=True)
    st.write("You may not need any treatment during the early stages of Parkinson's disease as symptoms are usually mild.")
    st.write("But you may need regular appointments with your specialist so your condition can be monitored.")
    st.write("You might be offered a device to wear at home that monitors your symptoms. The device shares relevant information with your specialist.")
    st.write('A care plan should be agreed with your healthcare team and your family or carers.')
    st.write("This will outline the treatments and help you need now and what you're likely to need in the future, and should be reviewed regularly.")
    st.markdown("[NICE guideline for Parkinson’s disease](https://www.nice.org.uk/guidance/ng71/ifp/chapter/Parkinsons-disease-the-care-you-should-expect)")
    st.subheader("Supportive therapies")
    st.write("There are several therapies that can make living with Parkinson's disease easier and help you deal with your symptoms on a day-to-day basis.")
    st.write("There are efforts underway to try to increase the availability of these supportive therapies for Parkinson's patients on the NHS.")
    st.write('Your local authority may be able to advise and help you. Ask your local authority for a care and support needs assessment.')
    st.markdown("[Care and support plans](https://www.nhs.uk/conditions/social-care-and-support-guide/help-from-social-services-and-charities/care-and-support-plans/)")
    st.subheader("Physiotherapy")
    st.write('A physiotherapist can work with you to relieve muscle stiffness and joint pain through movement (manipulation) and exercise.')
    st.write('The physiotherapist aims to make moving easier and improve your walking and flexibility.')
    st.write('They also try to improve your fitness levels and ability to manage things for yourself.')
    st.markdown( "[Find out more about Physiotherapy ](https://www.nhs.uk/conditions/physiotherapy/)")
    st.subheader("Occupational therapy")
    st.write('An occupational therapist can identify areas of difficulty in your everyday life, such as dressing yourself or getting to the local shops.')
    st.write('They can help you work out practical solutions and ensure your home is safe and properly set up for you. This will help you maintain your independence for as long as possible.')
    st.markdown("[Find out more about Occupational therapy](https://www.nhs.uk/conditions/occupational-therapy/)")
    st.subheader("Speech and language therapy")
    st.write('An occupational therapist can identify areas of difficulty in your everyday life, such as dressing yourself or getting to the local shops.')
    st.write("Many people with Parkinson's disease have swallowing difficulties (dysphagia) and problems with their speech.")
    st.write("A speech and language therapist can often help you improve these problems by teaching speaking and swallowing exercises, or by providing assistive technology.")
    st.subheader("Diet advice")
    st.write("For some people with Parkinson's disease, making dietary changes can help improve some symptoms.")
    st.write("These changes can include:")
    st.markdown("- increasing the amount of fibre in your diet and making sure you're drinking enough fluid to reduce constipation")
    st.markdown("- increasing the amount of salt in your diet and eating small, frequent meals to avoid problems with low blood pressure, such as dizziness when you stand up quickly")
    st.markdown("- making changes to your diet to avoid unintentional weight loss")
    st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
    st.write("You may see a dietitian, a healthcare professional trained to give diet advice, if your care team thinks you may benefit from changing your diet.")
    st.subheader("Medication")
    st.write("Medication can be used to improve the main symptoms of Parkinson's disease, such as shaking (tremors) and movement problems.")
    st.write("But not all the medications available are useful for everyone, and the short- and long-term effects of each are different.")
    st.write("Three main types of medication are commonly used:")
    st.markdown("- levodopa")
    st.markdown( "- dopamine agonists")
    st.markdown("- monoamine oxidase-B inhibitors")
    st.markdown('''
                        <style>
                        [data-testid="stMarkdownContainer"] ul{
                            padding-left:40px;
                        }
                        </style>
                        ''', unsafe_allow_html=True)
    st.write("Your specialist can explain your medication options, including the risks associated with each medication, and discuss which may be best for you.")
    st.write("Regular reviews will be required as the condition progresses and your needs change.")
    st.subheader("Levodopa")
    st.write("Most people with Parkinson's disease eventually need a medication called levodopa.")
    st.write("Levodopa is absorbed by the nerve cells in your brain and turned into the chemical dopamine, which is used to transmit messages between the parts of the brain and nerves that control movement.")
    st.write("Increasing the levels of dopamine using levodopa usually improves movement problems.")
    st.write("It's usually taken as a tablet or liquid, and is often combined with other medication, such as benserazide or carbidopa.")
    st.write("These medications stop the levodopa being broken down in the bloodstream before it has a chance to get to the brain.")
    st.write("They also reduce the side effects of levodopa, which include:")
    st.markdown("- feeling and being sick")
    st.markdown("- tiredness")
    st.markdown("- dizziness")
    st.markdown('''
                            <style>
                            [data-testid="stMarkdownContainer"] ul{
                                padding-left:40px;
                            }
                            </style>
                            ''', unsafe_allow_html=True)
    st.write("If you're prescribed levodopa, the initial dose is usually very small and will be gradually increased until it takes effect.")
    st.write("At first, levodopa can cause a dramatic improvement in the symptoms.")
    st.write("But its effects can be less long-lasting over the following years – as more nerve cells in the brain are lost, there are fewer of them to absorb the medicine.")
    st.write("This means the dose may need to be increased from time to time.")
    st.write('Long-term use of levodopa is also linked to problems such as uncontrollable, jerky muscle movements (dyskinesias) and "on-off" effects, where the person rapidly switches between being able to move (on) and being immobile (off).')
    st.subheader("Dopamine agonists")
    st.write("Dopamine agonists act as a substitute for dopamine in the brain and have a similar but milder effect compared with levodopa. They can often be given less frequently than levodopa.")
    st.write("They're often taken as a tablet, but are also available as a skin patch (rotigotine).")
    st.write("Sometimes dopamine agonists are taken at the same time as levodopa, as this allows lower doses of levodopa to be used.")
    st.write("Possible side effects of dopamine agonists include:")
    st.markdown("- feeling and being sick")
    st.markdown("- tiredness and sleepiness")
    st.markdown("- dizziness")
    st.markdown('''
                               <style>
                               [data-testid="stMarkdownContainer"] ul{
                                   padding-left:40px;
                               }
                               </style>
                               ''', unsafe_allow_html=True)
    st.write("Dopamine agonists can also cause hallucinations and increased confusion, so they need to be used with caution, particularly in elderly patients, who are more susceptible.")
    st.write("For some people, dopamine agonists have been linked to the development of compulsive behaviours, especially at high doses, including addictive gambling, compulsive shopping and an excessively increased interest in sex.")
    st.write("Talk to your healthcare specialist if you think you may be experiencing these problems.")
    st.write("As the person themselves may not realise the problem, it's key that carers and family members also note any abnormal behaviour and discuss it with an appropriate professional at the earliest opportunity.")
    st.write("If you're prescribed a course of dopamine agonists, the initial dose is usually very small to prevent feeling sick and other side effects.")
    st.write("The dosage is gradually increased over a few weeks. If feeling sick becomes a problem, your GP may prescribe anti-sickness medication.")
    st.write("A potentially serious, but uncommon, complication of dopamine agonist therapy is sudden onset of sleep.")
    st.write("This generally happens as the dose is being increased and tends to settle once the dose is stable.")
    st.write("People are usually advised to avoid driving while the dose is being increased in case this complication occurs.")
    st.subheader("Monoamine oxidase-B inhibitors")
    st.write("Monoamine oxidase-B (MAO-B) inhibitors, including selegiline and rasagiline, are another alternative to levodopa for treating early Parkinson's disease.")
    st.write("They block the effects of an enzyme or brain substance that breaks down dopamine (monoamine oxidase-B), increasing dopamine levels.")
    st.write("Both selegiline and rasagiline can improve the symptoms of Parkinson's disease, although their effects are small compared with levodopa. They can be used alongside levodopa or dopamine agonists.")
    st.write("MAO-B inhibitors are generally very well tolerated, but can occasionally cause side effects, including:")
    st.markdown("- feeling sick")
    st.markdown("- headaches")
    st.markdown("- abdominal pain")
    st.markdown("- high or low blood pressure")
    st.markdown('''
                                   <style>
                                   [data-testid="stMarkdownContainer"] ul{
                                       padding-left:40px;
                                   }
                                   </style>
                                   ''', unsafe_allow_html=True)
    st.subheader("Surgery")
    st.write("Most people with Parkinson's disease are treated with medication, although a type of surgery called deep brain stimulation is used in some cases.")
    st.write("This surgery is also available in specialist neuroscience centres around the UK, but it's not suitable for everyone.")
    st.write("If surgery is being considered, your specialist will discuss the possible risks and benefits with you.")
    st.subheader("Deep brain stimulation")
    st.write("Deep brain stimulation involves surgically implanting a pulse generator similar to a heart pacemaker into your chest wall.")
    st.write("This is connected to 1 or 2 fine wires placed under the skin, and is inserted precisely into specific areas in your brain.")
    st.write("A tiny electric current is produced by the pulse generator, which runs through the wire and stimulates the part of your brain affected by Parkinson's disease.")
    st.write("Although surgery does not cure Parkinson's disease, it can ease the symptoms for some people.")
    st.subheader("Complementary and alternative therapies")
    st.write("Some people with Parkinson's disease find complementary therapies help them feel better.")
    st.write("Many complementary treatments and therapies claim to ease the symptoms of Parkinson's disease.")
    st.write("But there's no clinical evidence they're effective at controlling the symptoms of Parkinson's disease.")
    st.write("Most people think complementary treatments have no harmful effects. But some can be harmful and should not be used instead of the medicines prescribed by your doctor.")
    st.write("Some types of herbal remedies, such as St John's wort, can interact unpredictably if taken with some types of medication used to treat Parkinson's disease.")
    st.write("If you're considering using an alternative treatment along with your prescribed medicines, check with your care team first.")
# Parkinsons Prediction Page
if (selected == 'Parkinson\'s Prediction'):    
    
    # page title
    st.title("Parkinson's Disease Prediction ")
    img = Image.open('Parkinsons.jpg')
    st.image(img)
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.warning("Please fill in all the fields.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



    




    






    
    
    
    
    
    
    
