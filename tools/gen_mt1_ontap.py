# -*- coding: utf-8 -*-
"""Chuyển đổi 1 lần: 4 file đề cương (src/mt1/dc2223.txt, dc2324.txt, dc2425.txt, tn.txt)
-> units/mt1_ontap.py (SET) + units/mt1_ontap_dapan.py (ANS + EXPLANATIONS).
Nguồn Word không có khoá đáp án => toàn bộ đáp án/giải thích được soạn tay (tự giải độc lập) trong file này.
Nguồn s: '2223' (dc2223), '2324' (dc2324), '2425' (dc2425), 'tn' (tn.txt).
Bước: (1) khai báo toàn bộ mục từ gốc  (2) loại trùng (chuẩn hoá chữ thường, bỏ khoảng trắng + dấu câu; thêm so khớp mờ)
(3) gán id  (4) chọn 40 câu cho bài kiểm tra  (5) ghi file."""
import re, os, sys, difflib, pprint
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW = []          # danh sách mục gốc theo thứ tự khai báo
GHI = []          # GHI_CHU_RA_SOAT
GROUPS = {}       # gid -> dict
PAGES = []        # (pid, title)


def PAGE(pid, title):
    PAGES.append((pid, title))


def G(gid, page, instr, passage='', note='', bank=None):
    GROUPS[gid] = {'id': gid, 'page': page, 'instr': instr, 'passage': passage, 'note': note, 'bank': bank}


def N(s):
    GHI.append(s)


def _add(**k):
    RAW.append(k)


def M(g, s, q, opts, ans, exp, plain=False):
    _add(g=g, s=s, t='mcq', q=q, o=[x.strip() for x in opts.split('|')], ans=ans, exp=exp)


def F(g, s, q, ans, exp, hint=None):
    _add(g=g, s=s, t='fill', q=q, ans=ans, exp=exp, hint=hint)


def O(g, s, q, exp):
    _add(g=g, s=s, t='open', q=q, exp=exp)


def E(g, s, text, ans, exp):
    """câu tìm lỗi sai: các đoạn <u>..</u> theo thứ tự = A,B,C,D"""
    segs = re.findall(r'<u>(.*?)</u>', text)
    assert len(segs) == 4, text
    it = iter('ABCD')
    q = re.sub(r'<u>(.*?)</u>', lambda m: '<u>%s</u><sup>%s</sup>' % (m.group(1), next(it)), text)
    _add(g=g, s=s, t='mcq', q=q, o=[x.strip() for x in segs], ans=ans, exp=exp)


def SND(g, s, opts, ans, exp):
    """câu phát âm/trọng âm không có thân câu"""
    _add(g=g, s=s, t='mcq', q='', o=[x.strip() for x in opts.split('|')], ans=ans, exp=exp)

# ======================================================================================
# KHAI BÁO TRANG + NHÓM
# ======================================================================================
PAGE('phat-am', 'Phát âm & trọng âm')
PAGE('tu-vung', 'Từ vựng')
PAGE('ngu-phap', 'Ngữ pháp')
PAGE('loi-sai', 'Tìm lỗi sai')
PAGE('dien-tu', 'Điền từ & sắp xếp câu')
PAGE('doc-hieu', 'Đọc hiểu')
PAGE('viet', 'Viết lại câu & viết đoạn')
PAGE('noi-giao-tiep', 'Nói & giao tiếp')

IN_SND = 'Choose the word whose underlined part is pronounced differently from that of the others.'
IN_STR = 'Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress.'
G('pa1', 'phat-am', IN_SND)
G('pa2', 'phat-am', IN_STR)
G('tv1', 'tu-vung', 'Choose the word or phrase which best completes each sentence (từ vựng, giới từ đi kèm, dạng từ).')
G('tv2', 'tu-vung', 'Mark the letter A, B, C, or D to indicate the word CLOSEST in meaning to the underlined word(s).')
G('tv3', 'tu-vung', 'Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s).')
G('tv4', 'tu-vung', 'Complete the sentences with the correct form of the words in brackets (dạng từ).')
G('ng1', 'ngu-phap', 'Quá khứ đơn và hiện tại hoàn thành: choose the best answer.')
G('ng2', 'ngu-phap', 'Động từ khuyết thiếu (should, ought to, must, have to, mustn\'t, needn\'t…): choose the best answer.')
G('ng3', 'ngu-phap', 'Động từ nối / động từ trạng thái / dạng từ / thể bị động: choose the best answer.')
G('ng4', 'ngu-phap', 'Write the correct form of the verbs in brackets.')
G('er1', 'loi-sai', 'Mark the letter A, B, C, or D to indicate the underlined part that needs correction.')
G('dt1', 'dien-tu', 'Read the passage and choose the best option to fill in each blank (Families).',
  '<p>Fathers in today families are spending more time with their children than at any point in the past 100 years. <b>(1) ______</b> the number of hours the average woman spends at home with her children has declined since the early 1900s, as more and more women enter the workforce, there has been a decrease in the number of children per family and an increase in <b>(2) ______</b> attention to each child. As a result, mothers today in the United States, <b>(3) ______</b> those who work part- or full-time, spend almost twice as much time with each child as mothers did in the 1920s. People <b>(4) ______</b> raised children in the 1940s and 1950s typically report that their own adult children and grandchildren communicate far better with their kids and spend more time <b>(5) ______</b> with homework than they did.</p>')
G('dt2', 'dien-tu', 'Read the passage and choose the best option to fill in each blank (Dutch children).',
  '<p><b>Dutch children enjoy their freedom</b></p><p>“Let them be free” is the <b>(1) ______</b> rule for child-rearing in the Netherlands. No wonder Dutch kids have been <b>(2) ______</b> Europe’s most fortunate. From a tender age, their opinions are <b>(3) ______</b> their wishes respected, and there is no homework until their last year in preparatory school. Some would <b>(4) ______</b> that the tendency of Dutch society to encourage infants to experience whatever they please has <b>(5) ______</b> a whole generation into spoilt, undisciplined brats.</p>')
G('dt3', 'dien-tu', 'Read the passage and choose the best option to fill in each blank (Dad).',
  '<p>In the home a dad is very important. He is the <b>(1) ______</b> who provides us with the money to feed and clothe ourselves. He can decorate your bedroom, mend your radio, make cages for your pets, repair a puncture in your bicycle tyre and help you with Maths homework. A dad can be very useful for <b>(2) ______</b> you in the car to and from parties, music and dancing lessons.</p><p>A dad is the person whom you ask for pocket money. He is the one who <b>(3) ______</b> about the time you spend talking on the phone, as he has to pay for the bills. Dad is someone who will <b>(4) ______</b> you in an argument, if he believes you to be right. He is someone who reads your school <b>(5) ______</b> and treats if it is good. A dad likes to come into a nice happy home evening, and settle back in his chair with a newspaper.</p>')
G('dt4', 'dien-tu', 'Read the passage and choose the best option to fill in each blank (Healthy relationship).',
  '<p>In a healthy relationship, both partners respect, trust and embrace <b>(1) ______</b> differences. Both partners are able to communicate <b>(2) ______</b> their needs and listen to their partner, and work to resolve conflict in a rational and <b>(3) ______</b> way. But maintaining a healthy relationship <b>(4) ______</b> skills many young people are never taught. A lack of these skills, and <b>(5) ______</b> up in a society that sometimes celebrates violence or in a community that experiences a high rate of violence, can lead to unhealthy and even violent relationships among youth.</p>')
G('dt5', 'dien-tu', 'Choose the word or phrase that best fits each blank in the passage (Exercise and character).',
  '<p>Everyone knows that exercise is good for the body and the mind. We all want to keep fit and look good, but too many of us take <b>(1) ______</b> the wrong sport and quickly lose interest. So now fitness experts are advising people to choose an activity that matches their character.</p><p>For instance, those <b>(2) ______</b> like to be with other people often enjoy golf or squash, or playing for a basketball, football, or hockey team. <b>(3) ______</b>, you may prefer to go jogging or swimming if you’re happier on your own.</p><p>Do you like competition? Then try something like running, or a racket sport such as tennis. If, on the other hand, <b>(4) ______</b> isn’t important to you, then activities like dancing can be an enjoyable <b>(5) ______</b> without the need to show you’re better than everyone else.</p><p>Finally, think about whether you find it easy to make yourself do exercise. If so, sports like weight training at home and cycling are fine. If not, book a skiing holiday, Taekwondo lessons, or a tennis court. You’re much more likely to do something you’ve already paid for!</p>')
G('dt6', 'dien-tu', 'Choose the word or phrase that best fits each blank in the passage (Driverless cars).',
  '<p>Driving along the motorway in busy traffic, the driver suddenly presses a button on his steering wheel. The car is now driving itself. This may <b>(1) ______</b> like something from the future, but driverless cars are already in reality on California’s roads. Many cars can already park themselves on the roadside, brake automatically when the car needs to slow down, and warn the driver <b>(2) ______</b> they are slipping out of the right lane, so going driverless is just the next step towards automated driving. Driverless cars are equipped with fast broadband, allowing them to overtake other cars <b>(3) ______</b>, and even communicate with traffic lights as they approach junctions. Being stuck in traffic jams could become a thing of the past, as driverless cars will be able to drive at speed <b>(4) ______</b> to each other. More than fifty million people die or are injured in road accidents every year, and the majority of these accidents is caused by human <b>(5) ______</b>. Google’s driverless car sticks to the speed limit and doesn’t get tired. Why wouldn’t it be a great idea if all cars were driverless?</p>')
G('dt7', 'dien-tu', 'Read the passage and choose the correct word or phrase for each blank (Living a healthy life).',
  '<p>Living a healthy life is very important for our well-being. When we are healthy, we feel <b>(1) ______</b> and can do things we enjoy. Eating healthy foods, like fruits and vegetables, helps our bodies stay strong and gives us energy. It is also important to exercise regularly, like <b>(2) ______</b> sports or going for walks, to keep our bodies active and fit. Getting enough sleep at night helps us feel rested and ready for the day. Taking <b>(3) ______</b> of our bodies and staying away from things <b>(4) ______</b> can harm us, like smoking or too much junk food, is important too. When we live a healthy life, we can have more fun, <b>(5) ______</b> happier, and enjoy life to the fullest.</p>')
G('dt8', 'dien-tu', 'Read the advertisement and choose the option that best fits each blank.',
  '<p><b>Find Your Inner Peace: Join Our Meditation Course Today!</b></p><p>Are you looking to reduce stress, improve focus, and enhance your overall well-being? Our expert-led meditation course is designed just for you! Over the course of five weeks, you will:</p><ul><li>Learn effective meditation techniques to calm your mind and body.</li><li>Develop a <b>(1) ______</b> practice that fits into your daily routine.</li><li>Experience the benefits of reduced anxiety and improved mental clarity.</li></ul><p>Join us now and take the first step towards a <b>(2) ______</b> and peaceful life. Sign up today and start your journey to inner tranquility!</p><p><b>Special Offer:</b> Enroll now and get a 10% discount on your first session! Visit our website or call us at 0123456789 to <b>(3) ______</b> your spot! Find your calm, one breath at a time.</p>')
G('dt9', 'dien-tu', 'Read the announcement and choose the option that best fits each blank.',
  '<p><b>Announcement: COVID-19 Vaccination for Students</b></p><p>Attention Students and Parents,</p><p>We are pleased to <b>(1) ______</b> that our school will be hosting a COVID-19 vaccination clinic to help protect our community. This initiative is aimed at ensuring the safety and health of our students as we navigate through these challenging times. The vaccination clinic will be held <b>(2) ______</b> March 15th from 9:00 AM to 3:00 PM at the school gymnasium.</p><p>To ensure a smooth process, we ask everyone to wear a mask, maintain social distancing, and arrive at their scheduled time to avoid crowding. It is also <b>(3) ______</b> to stay hydrated and have a light meal before coming.</p>')
G('dt10', 'dien-tu', 'Read the advertisement and choose the option that best fits each blank (Situation wanted).',
  '<p><b>SITUATION WANTED</b></p><p>A first class graduate in Physics from Delhi University with <b>(1) ______</b> experience of 7 years in teaching in <b>(2) ______</b> International schools seeks a job in or around Kolkata. B.Ed trained, Fluent <b>(3) ______</b> English, experienced in dealing with hundreds of students. Expected pay - 50,000.</p>')
G('dt11', 'dien-tu', 'Read the announcement of an airline and choose the option that best fits each blank.',
  '<p>Ladies and gentlemen, on behalf of the crew I ask that you please direct your attention to the monitors above as we review the emergency procedures. There are six emergency exits on this aircraft. <b>(1) ______</b> a minute to locate the exit closest to you. Note that the nearest exit may be behind you. Count the number of rows to this exit. <b>(2) ______</b> the cabin experience sudden pressure loss, stay calm and listen for instructions from the cabin crew. Oxygen masks will drop down from above your seat. Place the mask over your mouth and nose, like this. Pull the strap to tighten it. If you are traveling with children, make sure that your own mask is on first before helping your children. In the unlikely event of an emergency landing and evacuation, leave your carry-on items behind. Life rafts are located below your seats and emergency lighting will lead you to your closest exit and slide. We ask that you make sure that all carry-on luggage is stowed away safely during the flight. While we wait for <b>(3) ______</b>, please take a moment to review the safety data card in the seat pocket in front of you.</p>')
G('dt12', 'dien-tu', 'Read the passage and choose the correct word or phrase for each blank (The generation gap in Vietnam).',
  '<p>The generation gap in Vietnam presents <b>(1) ______</b> challenges and opportunities. With the rapid development and globalization, younger generations in Vietnam often have different values, attitudes, and aspirations <b>(2) ______</b> to older generations. This can lead to communication and understanding gaps between them. <b>(3) ______</b>, it also creates opportunities for mutual learning and growth. Younger generations bring fresh perspectives and ideas, while older generations offer wisdom and experience. <b>(4) ______</b> fostering open dialogue and embracing the diversity of viewpoints, Vietnam can <b>(5) ______</b> the positive aspects of the generation gap to drive social progress, economic development, and intergenerational harmony.</p>')
G('dt13', 'dien-tu', 'Mark the letter A, B, C, or D to indicate the correct arrangement of the sentences to make a meaningful paragraph/letter.')
G('dh1', 'doc-hieu', 'Read the passage and choose the correct answer to each question (Alternative schools).',
  '<p><b>ARE TRADITIONAL WAYS OF LEARNING THE BEST?</b></p><p>Read about some alternative schools of thought…</p><p>One school in Hampshire, UK, offers 24-hour teaching. The children can decide when or if they come to school. The school is open from 7 a.m. to 10 p.m., for 364 days a year and provides online teaching throughout the night. The idea is that pupils don\'t have to come to school and they can decide when they want to study. Cheryl Heron, the head teacher, said “Some students learn better at night. Some students learn better in the morning.” Cheryl believes that if children are bored, they will not come to school. “Why must teaching only be conducted in a classroom? You can teach a child without him ever coming to school.”</p><p>Steiner schools encourage creativity and free thinking so children can study art, music and gardening as well as science and history. They don’t have to learn to read and write at an early age. At some Steiner schools the teachers can’t use textbooks. They talk to the children, who learn by listening. Every morning the children have to go to special music and movement classes called “eurhythmy”, which help them learn to concentrate. Very young children learn foreign languages through music and song. Another difference from traditional schools is that at Steiner schools you don\'t have to do any tests or exams.</p><p>A child learning music with the Suzuki method has to start as young as possible. Even two-year-old children can learn to play difficult pieces of classical music, often on the violin. They do <b><u>this</u></b> by watching and listening. They learn by copying, just like they learn their mother tongue. The child has to join in, but doesn\'t have to get it right. “They soon learn that they mustn\'t stop every time they make a mistake. They just carry on,” said one Suzuki trainer. The children have to practise for hours every day and they give performances once a week, so they learn quickly. “The parents must be <b><u>involved</u></b> too,” said the trainer, “or it just doesn\'t work.”</p>')
G('dh2', 'doc-hieu', 'Read the passage and choose the correct answer to each question (Relationships and teenagers).',
  '<p>Different relationships affect teenagers in various ways. Friends impact teenagers almost the same amount as their parents. Teenagers go to their friends for help or to ask questions that they could not ask their parents about. Most of their friends give them good advice. In most cases, they tell their friends how to dress and act when being around certain people. Love relationships just make it even harder for a teenager to get a good education. Some start to fail in school because they are hanging out with their boyfriend or girlfriend instead of doing their work.</p><p>Parents have a big influence on teenagers because their children look up to them and the majority of them grow up to act and do things just like their parents did with them. Children who have experienced a family break-up may have lower achievements than children brought up in an intact family. As previously stated, teenagers are affected by many relationships which involve their friends, family, and their love relationships. The relationships affect them so much that most teenagers change their ideas about how they should live their lives in a different way and to change their future goals. They should be influenced to help themselves or to help others.</p>')
G('dh3', 'doc-hieu', 'Read the passage and choose the correct answer to each question (Online dating).',
  '<p>It has long been seen as a less romantic way of meeting <b><u>Mr. Right</u></b>. But finding love over the internet is a good way of meeting a marriage partner, research has showed. It found that one in five of those who have used dating sites to find their perfect partner have gone on to marry someone they met over the web. The study also revealed that more than half of the 1,504 people questioned had been on a date with someone they met in cyberspace. Sixty-two per cent agreed that it was easier to meet someone on a dating site than in other ways, such as in a pub or club, or through friends. At the same time, the under-35s were more likely to know someone who had been on a date or had a long-term relationship with someone they met through online dating.</p><p>Jess Ross, editor of WHICH.co.uk, said: \'Online dating is revolutionizing the way people meet each other. Switching the computer on could be the first step to success.\'</p><p>According to industry surveys, more than 22 million people visited dating websites in 2007 and more than two million Britons are signed up to singles sites.</p><p>Of the 147 couples who took part in the study, 61 per cent said their relationships had high levels of these three components. The researchers also found that men were more likely to find true love on the internet than women. Dr. Jeff Gavin, who led the team, said: \'To date, there has been no systematic study of love in the context of relationships formed via online dating sites. But with the popularity of online dating, it is <b>imperative</b> we understand the factors that influence satisfaction in relationships formed in this way.\'</p>')
G('dh4', 'doc-hieu', 'Read the passage and choose the correct answer to each question (College life skills).',
  '<p>The skills needed to succeed in college are very different from those required in high school. In addition to study skills that may be new to students, there will also be everyday living skills that students may not have had to use before.</p><p>Students should:</p><ul><li>know how to handle everyday living skills such as doing laundry, paying bills, balancing a checkbook, cooking, getting the oil changed in the car, etc.</li><li>be familiar and compliant with medical needs concerning medication and health problems. If <b>ongoing</b> medical and/or psychological treatment is needed, arrangements should be made in advance to continue that care while the student is away at college.</li><li>understand that the environmental, academic, and social structure provided by parents and teachers will not be in place in college. With this lack of structure comes an increased need for responsibility in decision-making and goal-setting.</li><li>know how to interact appropriately with instructors, college staff, roommates, and peers. Appropriate social interaction and communication are essential at the college level of education.</li><li>be comfortable asking for help when needed. The transition from high school to college can be <b>overwhelming</b> socially and academically. Students should know when they need help and should be able to reach out and ask for that help.</li></ul>')
G('dh5', 'doc-hieu', 'Read the passage and choose the correct answer to each question (The generation gap in America).',
  '<p>Is the generation gap in America no longer a severe problem as it used to be? Dating back to the 1960s when teenagers tended to lash out the values and goals of their parents as well as rebel against the authority figures, the incendiary conflicts between older and younger generations increased sharply. It’s because teenagers\' world wasn’t any longer limited in a narrow society that wasn’t mobile, and instead of going to church every weekend, they were exposed to various forms of social media like television and radios. <b>They</b> got access to huge sources of new ideas, which liberated them from old-fashioned and boring lifestyles whereas many older people were conservative and didn’t accept differences disturbing their normal life. Over time, however, the tension between generations has been alleviated due to the improved mutual understanding of baby boomers, Millennials and even Zillennials in many fields of life. According to recent research, the largest generational discrepancies between young and old in the United States are the use of technology and taste in music. Nevertheless, in terms of technological use, many older people gradually learn how to use a laptop or smartphone to surf the Internet from their children and especially their grandchildren due to their recognition of huge technological benefits. Regarding the musical differences, unlike in the past, older generations nowadays appear to give fewer critical remarks on what type of music teens should listen to and begin to accept the variety of music tastes when living under the same roofs.</p>')
G('dh6', 'doc-hieu', 'Read the text and choose the correct answer to each question (Parents and teens).',
  '<p>The family dynamic evolves as a teen matures and can test the parent-teen relationship. With both sides feeling mixed emotions, this time can be challenging.</p><p>Puberty brings lots of emotions for teens and is a time of readjustment for the whole family. Parents have a huge influence on a young child’s values and interests, and so it can often feel hard for them to separate from their teen, who wants to develop their own identity and to have new freedoms. <b><u>This</u></b> may lead to conflict, as both parents and teens need time to figure out how to adapt the relationship.</p><p>As teens get older, it is important for them to take on responsibilities. This highlights the valuable contribution each family member makes to a home and teaches teens about what it’s like to be an adult. Setting clear rules about routine and home life helps teens to know what’s expected of them - even if they do complain or resist. Expectations go both ways, however, and so constant communication and flexibility, when necessary, will help avoid conflict.</p><p>It is important for parents and teens to overcome life’s many distractions in order to spend quality time together. For parents, maintaining a close relationship with a teen who is preprogrammed to separate from them can be tricky, but it helps to be present and <b><u>willing</u></b>. Talking about the things that are going well is as helpful as discussing areas of conflict.</p>')
G('dh7', 'doc-hieu', 'Read the text and choose the correct answer to each question (The best time to exercise).',
  '<p>We all know the importance of exercise as a healthy habit. But what\'s the best time to exercise? Research has shown that morning, afternoon, or evening workouts have their own benefits. When you work out in the morning, you burn more fat. In fact, those who start their exercise routine on an empty stomach can burn about 20 percent more body fat than those exercising later in the day. Morning exercise also helps many people sleep better at night.</p><p>Afternoon or evening workouts can also bring benefits. Remember that your temperature is the highest between 2 p.m. and 6 p.m. This temperature helps increase your muscle strength and <b>endurance</b>. In the afternoon or evening, your reaction time is at <b>its</b> quickest, while your heart rate and blood pressure are the lowest. Exercising at this time decreases your chances of injury while improving your performance. So, depending on your schedule and preferences, you can choose the best time to work out.</p>')
G('dh8', 'doc-hieu', 'Read the passage and choose the correct answer to each question (Super Size Me).',
  '<p>Super Size Me is a 2004 film by Morgan Spurlock, in which he documents his experiment to eat only McDonald\'s fast food three times a day, every day, for thirty days.</p><p>Spurlock made himself a short list of rules for the experiment, including an obligation to eat all of the three meals he ordered. He also had to ‘Super Size’, which means accepting a <b>giant</b> portion every time the option was offered to him. He ended up vomiting after the first Super Size meal he finished, after taking nearly twenty minutes to consume it.</p><p>After five days Spurlock put on almost 5kg, and he soon found himself feeling depressed, with no energy. The only thing that got rid of his headaches and made him feel better was another McDonald\'s meal, so his doctors told him he was addicted. More seriously, around day twenty, he started experiencing heart palpitations and one of the doctors detected liver problems. However, in spite of his doctor\'s advice, Spurlock continued to the end of the month and achieved a total weight gain of 11kg. His body mass index also increased from a healthy 23.2 to an overweight 27.</p><p>It took Spurlock fifteen months to recover from his experiment and return to his original weight, but the film also had a wider impact. Just after <b>its</b> showing in 2004, McDonald\'s phased out the Super Size option and healthier options like salads appeared on the menu. Unfortunately, McDonald\'s denied the connection between the film and the changes, but it is interesting to note how closely they coincided with the release of the film.</p>')
G('dh9', 'doc-hieu', 'Read the passage and choose the correct answer to each question (Generation gap at work).',
  '<p>The generation gap in the business world is a fascinating phenomenon that highlights the differences in attitudes, values, and approaches to conducting business between different generations. One of the key areas where the generation gap is evident is in technology adoption. Younger generations, such as Millennials and Generation Z, have grown up in the digital age and are generally more comfortable with technology. <b><u>They</u></b> readily embrace new tools, platforms, and digital strategies, which can significantly impact business practices, marketing strategies, and communication methods.</p><p>Workforce expectations also play a crucial role in the generation gap. Each generation has its own set of expectations when it comes to work-life balance, career progression, and job satisfaction. Younger generations often prioritize flexibility, purpose-driven work, and a healthy work-life balance. Meanwhile, older generations may place more emphasis on job stability, loyalty, and traditional career paths. Leadership styles are another area where the generation gap becomes evident. Baby Boomers and Generation X typically favor hierarchical structures and a more top-down management style. They are used to a more authoritative approach to leadership. Conversely, younger generations often prefer collaborative and inclusive leadership styles, valuing input from all levels of the organization. They <b><u>thrive</u></b> in environments that encourage participation, teamwork, and innovation. Communication preferences have also evolved with each generation. The way people communicate and consume information has drastically changed over the years. Younger generations are inclined towards instant messaging, social media, and other digital channels for communication.</p><p><i>(Adapted from “Generation Gap at Work - Reshaping the Workplace”)</i></p>')
G('dh10', 'doc-hieu', 'Read the passage and choose the correct answer to each question (The invention of Coca-Cola).',
  '<p>It is not surprising that the birthplace of cola was the hot and humid American South. This region had long specialized in creating delicious soft drinks. A druggist in Atlanta, Georgia named John Pemberton created the most well-known drink brand in the world in the 1880s. However, it seems clear that he had no idea how big it would become.</p><p>Like many American pharmacists of the day, Pemberton was opposed to the drinking of alcohol and wanted to produce a stimulating soft drink. First, he made “the French Wine of Coca,” made from the coca leaf. Then he began to experiment with the cola nut. Eventually, he managed to make a combination of the two that he thought was sweet, but not too sweet. Deciding that “the two C’s would look well in advertising,” <b><u>he</u></b> named it Coca-Cola.</p><p>Pemberton\'s invention <b><u>caught on</u></b> fairly quickly. By 1905, “Coke” was being advertised all over the country as “The Great Natural Temperance Drink.” The drink enjoyed additional success since there was a large and popular temperance movement in the US at that time. In the 1920s, alcohol was <b><u>outlawed</u></b>, and sales of Coke rose significantly. However, they continued to rise even after the law was repealed. Another reason for Coke\'s popularity was good business sense. A year after he invented it, Pemberton had sold Coca-Cola to Asa Griggs Candler for only $283.26! Candler was a marketing genius, and by the time he sold the Coca-Cola Company in 1919, it was worth $25 million.</p>')
G('vi1', 'viet', 'Rewrite the sentences (thì hiện tại hoàn thành / quá khứ đơn): complete the second sentence so that it has the same meaning as the first.')
G('vi2', 'viet', 'Rewrite the sentences using modal verbs: complete the second sentence so that it has the same meaning as the first.')
G('vi3', 'viet', 'Make sentences with the cues given (viết câu hoàn chỉnh từ từ gợi ý; không chấm điểm, xem đáp án mẫu).')
G('vi4', 'viet', 'Write a paragraph / an essay (viết đoạn văn; không chấm điểm, xem bài mẫu để đối chiếu).')
G('gt1', 'noi-giao-tiep', 'Choose the best response.')
G('gt2', 'noi-giao-tiep', 'Make a polite request for permission with the cues given (Do you mind if… / Would you mind if… / Can I…?). Không chấm điểm, xem đáp án mẫu.')
G('gt3', 'noi-giao-tiep', 'Speaking: trả lời các câu hỏi / nói theo chủ đề (không chấm điểm; xem gợi ý mẫu).')

# ======================================================================================
# PHÁT ÂM (sounds)
# ======================================================================================
SND('pa1', '2223', '<u>s</u>ure|<u>s</u>oup|<u>s</u>ugar|ma<u>ch</u>ine', 'B', 'sure /ʃʊə/, sugar /ˈʃʊɡə/, machine /məˈʃiːn/ → đều /ʃ/; soup /suːp/ → /s/. Chọn <b>soup</b>.')
SND('pa1', '2223', 'stud<u>y</u>|read<u>y</u>|pupp<u>y</u>|occup<u>y</u>', 'D', 'study /ˈstʌdi/, ready /ˈredi/, puppy /ˈpʌpi/ → -y đọc /i/; occupy /ˈɒkjupaɪ/ → -y đọc /aɪ/. Chọn <b>occupy</b>.')
SND('pa1', '2223', 'm<u>ai</u>ntain|g<u>a</u>me|integr<u>a</u>te|tr<u>a</u>dition', 'D', 'maintain /meɪnˈteɪn/, game /ɡeɪm/, integrate /ˈɪntɪɡreɪt/ → /eɪ/; tradition /trəˈdɪʃn/ → /ə/. Chọn <b>tradition</b>.')
SND('pa1', '2223', 'f<u>o</u>llow|r<u>o</u>mantic|pr<u>o</u>blem|c<u>o</u>nfident', 'B', 'follow /ˈfɒləʊ/ (o đầu), problem /ˈprɒbləm/, confident /ˈkɒnfɪdənt/ → /ɒ/; romantic /rəʊˈmæntɪk/ → /əʊ/. Chọn <b>romantic</b>.')
SND('pa1', '2223', 'c<u>a</u>sual|fl<u>a</u>shy|<u>a</u>ttitude|t<u>a</u>ble', 'D', 'casual /ˈkæʒuəl/, flashy /ˈflæʃi/, attitude /ˈætɪtjuːd/ → /æ/; table /ˈteɪbl/ → /eɪ/. Chọn <b>table</b>.')
SND('pa1', '2223', 'am<u>a</u>zing|ch<u>a</u>rge|fem<u>a</u>le|t<u>a</u>ste', 'B', 'amazing /əˈmeɪzɪŋ/, female /ˈfiːmeɪl/, taste /teɪst/ → /eɪ/; charge /tʃɑːdʒ/ → /ɑː/. Chọn <b>charge</b>.')
SND('pa1', '2223', 'b<u>e</u>lief|g<u>e</u>neration|ext<u>e</u>nded|<u>e</u>legant', 'A', 'belief /bɪˈliːf/ → /ɪ/; generation /ˌdʒenəˈreɪʃn/, extended /ɪkˈstendɪd/, elegant /ˈelɪɡənt/ → /e/. Chọn <b>belief</b>.')
SND('pa1', '2223', '<u>a</u>chievement|<u>a</u>ppearance|enthusi<u>a</u>stic|initi<u>a</u>tive', 'C', 'achievement /əˈtʃiːvmənt/, appearance /əˈpɪərəns/, initiative /ɪˈnɪʃətɪv/ → /ə/; enthusiastic /ɪnˌθjuːziˈæstɪk/ → /æ/. Chọn <b>enthusiastic</b>.')
SND('pa1', 'tn', 'fr<u>e</u>sh|di<u>e</u>t|fl<u>e</u>sh|<u>e</u>xercise', 'B', 'fresh /freʃ/, flesh /fleʃ/, exercise /ˈeksəsaɪz/ → /e/; diet /ˈdaɪət/ → /aɪə/. Chọn <b>diet</b>.')
SND('pa1', 'tn', 'Yog<u>a</u>|f<u>a</u>tty|b<u>a</u>lance|h<u>a</u>bit', 'A', 'yoga /ˈjəʊɡə/ → /ə/; fatty /ˈfæti/, balance /ˈbæləns/, habit /ˈhæbɪt/ → /æ/. Chọn <b>yoga</b>.')
SND('pa1', 'tn', '<u>i</u>ngredient|nutr<u>i</u>ent|v<u>i</u>tamin|m<u>i</u>neral', 'B', 'ingredient /ɪnˈɡriːdiənt/, vitamin /ˈvɪtəmɪn/, mineral /ˈmɪnərəl/ → /ɪ/; nutrient /ˈnjuːtriənt/ → i đọc /i/ (nutri-ent). Chọn <b>nutrient</b>.')
SND('pa1', 'tn', '<u>g</u>ap|<u>g</u>eneration|<u>g</u>randparent|<u>g</u>reat', 'B', 'gap, grandparent, great → /ɡ/; generation /ˌdʒenəˈreɪʃn/ → /dʒ/. Chọn <b>generation</b>.')
SND('pa1', 'tn', 'h<u>o</u>ld|foll<u>o</u>w|f<u>o</u>rce|n<u>o</u>tice', 'C', 'hold /həʊld/, follow /ˈfɒləʊ/ (o cuối), notice /ˈnəʊtɪs/ → /əʊ/; force /fɔːs/ → /ɔː/. Chọn <b>force</b>.')
SND('pa1', 'tn', 'f<u>oo</u>tstep|r<u>oo</u>f|f<u>oo</u>d|f<u>oo</u>l', 'A', 'footstep /ˈfʊtstep/ → /ʊ/; roof /ruːf/, food /fuːd/, fool /fuːl/ → /uː/. Chọn <b>footstep</b>.')
SND('pa1', 'tn', 'b<u>e</u>lieve|<u>e</u>xtend|r<u>e</u>spect|g<u>e</u>nder', 'D', 'believe /bɪˈliːv/, extend /ɪkˈstend/, respect /rɪˈspekt/ → /ɪ/; gender /ˈdʒendə/ → /e/. Chọn <b>gender</b>.')
SND('pa1', 'tn', 'spe<u>c</u>ial|<u>c</u>ommon|<u>c</u>onsist|<u>c</u>onflict', 'A', 'special /ˈspeʃl/ → c đọc /ʃ/; common, consist, conflict → c đọc /k/. Chọn <b>special</b>.')
SND('pa1', 'tn', 'dw<u>e</u>ller|s<u>e</u>nsor|<u>e</u>nergy|r<u>e</u>duce', 'D', 'dweller /ˈdwelə/, sensor /ˈsensə/, energy /ˈenədʒi/ → /e/; reduce /rɪˈdjuːs/ → /ɪ/. Chọn <b>reduce</b>.')
SND('pa1', 'tn', 'des<u>i</u>gn|<u>i</u>mpact|publ<u>i</u>c|traff<u>i</u>c', 'A', 'design /dɪˈzaɪn/ → i đọc /aɪ/; impact /ˈɪmpækt/, public /ˈpʌblɪk/, traffic /ˈtræfɪk/ → /ɪ/. Chọn <b>design</b>.')
SND('pa1', '2425', 'h<u>ea</u>lthy|fitn<u>e</u>ss|str<u>e</u>ngth|m<u>e</u>ntal', 'B', 'healthy /ˈhelθi/, strength /streŋθ/, mental /ˈmentl/ → /e/; fitness /ˈfɪtnəs/ → /ɪ/ (hoặc /ə/). Chọn <b>fitness</b>.')
SND('pa1', '2425', 'heal<u>th</u>|en<u>th</u>usiasm|streng<u>th</u>|wi<u>th</u>out', 'D', 'health /helθ/, enthusiasm /ɪnˈθjuːziæzəm/, strength /streŋθ/ → /θ/; without /wɪˈðaʊt/ → /ð/. Chọn <b>without</b>.')
SND('pa1', '2425', '<u>g</u>ap|<u>g</u>eneration|<u>g</u>randparent|<u>g</u>reat', 'B', 'gap, grandparent, great → /ɡ/; generation → /dʒ/. Chọn <b>generation</b>.')
SND('pa1', '2425', 'g<u>a</u>p|<u>a</u>pplication|v<u>a</u>lue|beh<u>a</u>vior', 'D', 'gap /ɡæp/, application /ˌæplɪˈkeɪʃn/, value /ˈvæljuː/ → /æ/; behavior /bɪˈheɪvjə/ → /eɪ/. Chọn <b>behavior</b>.')
SND('pa1', '2425', 'h<u>o</u>ld|foll<u>o</u>w|f<u>o</u>rce|N<u>o</u>tice', 'C', 'hold, follow, notice → /əʊ/; force → /ɔː/. Chọn <b>force</b>.')
SND('pa1', '2425', 'dw<u>e</u>ller|s<u>e</u>nsor|<u>e</u>nergy|r<u>e</u>duce', 'D', 'dweller, sensor, energy → /e/; reduce → /ɪ/. Chọn <b>reduce</b>.')
SND('pa1', '2425', 'des<u>i</u>gn|<u>i</u>mpact|publ<u>i</u>c|traff<u>i</u>c', 'A', 'design → /aɪ/; impact, public, traffic → /ɪ/. Chọn <b>design</b>.')
SND('pa1', '2425', '<u>e</u>xtend|b<u>e</u>tween|b<u>e</u>lieve|m<u>e</u>mber', 'D', 'extend /ɪkˈstend/, between /bɪˈtwiːn/, believe /bɪˈliːv/ → /ɪ/; member /ˈmembə/ → /e/. Chọn <b>member</b>.')
SND('pa1', '2425', 'a<u>cc</u>ept|nu<u>c</u>lear|dis<u>c</u>uss|in<u>c</u>lude', 'A', 'accept /əkˈsept/ → cc đọc /ks/; nuclear /ˈnjuːkliə/, discuss /dɪˈskʌs/, include /ɪnˈkluːd/ → c đọc /k/. Chọn <b>accept</b>.')
N('pa1 (tn "hold/follow/force/notice"): chữ gạch chân của "follow" là o CUỐI (/əʊ/) → khoá = force (C); nguồn không có khoá, tự giải.')
N('pa1 (tn "nutrient"): i trong nutrient đọc /i/ (khác /ɪ/ của ingredient, vitamin, mineral) – giữ khoá B, hơi tinh tế.')

# --- trọng âm
SND('pa2', '2324', 'prevent|injure|balance|suffer', 'A', 'prevent /prɪˈvent/ nhấn âm 2; injure /ˈɪndʒə/, balance /ˈbæləns/, suffer /ˈsʌfə/ nhấn âm 1. Chọn <b>prevent</b>.')
SND('pa2', '2324', 'fitness|disease|treatment|headache', 'B', 'disease /dɪˈziːz/ nhấn âm 2; fitness /ˈfɪtnəs/, treatment /ˈtriːtmənt/, headache /ˈhedeɪk/ nhấn âm 1. Chọn <b>disease</b>.')
SND('pa2', '2324', 'longer|fatal|immune|careful', 'C', 'immune /ɪˈmjuːn/ nhấn âm 2; longer, fatal /ˈfeɪtl/, careful /ˈkeəfl/ nhấn âm 1. Chọn <b>immune</b>.')
SND('pa2', '2324', 'infectious|essential|resistant|properly', 'D', 'infectious /ɪnˈfekʃəs/, essential /ɪˈsenʃl/, resistant /rɪˈzɪstənt/ nhấn âm 2; properly /ˈprɒpəli/ nhấn âm 1. Chọn <b>properly</b>.')
SND('pa2', '2324', 'nutrient|vitamin|mineral|infection', 'D', 'infection /ɪnˈfekʃn/ nhấn âm 2; nutrient /ˈnjuːtriənt/, vitamin /ˈvɪtəmɪn/, mineral /ˈmɪnərəl/ nhấn âm 1. Chọn <b>infection</b>.')
SND('pa2', '2324', 'expression|example|friendliness|superior', 'C', 'expression /ɪkˈspreʃn/, example /ɪɡˈzɑːmpl/, superior /suːˈpɪəriə/ nhấn âm 2; friendliness /ˈfrendlinəs/ nhấn âm 1. Chọn <b>friendliness</b>.')
SND('pa2', '2324', 'value|afford|depend|impose', 'A', 'value /ˈvæljuː/ nhấn âm 1; afford /əˈfɔːd/, depend /dɪˈpend/, impose /ɪmˈpəʊz/ nhấn âm 2. Chọn <b>value</b>.')
SND('pa2', '2324', 'influence|attitude|counselor|decision', 'D', 'influence /ˈɪnfluəns/, attitude /ˈætɪtjuːd/, counselor /ˈkaʊnsələ/ nhấn âm 1; decision /dɪˈsɪʒn/ nhấn âm 2. Chọn <b>decision</b>.')
SND('pa2', '2324', 'donate|compare|campaign|limit', 'D', 'donate /dəʊˈneɪt/, compare /kəmˈpeə/, campaign /kæmˈpeɪn/ nhấn âm 2; limit /ˈlɪmɪt/ nhấn âm 1. Chọn <b>limit</b>.')
SND('pa2', '2324', 'experience|mobility|independence|priorities', 'C', 'experience /ɪkˈspɪəriəns/, mobility /məʊˈbɪləti/, priorities /praɪˈɒrətiz/ nhấn âm 2; independence /ˌɪndɪˈpendəns/ nhấn âm 3. Chọn <b>independence</b>.')
SND('pa2', '2324', 'romantic|infectious|protective|elegant', 'D', 'romantic /rəʊˈmæntɪk/, infectious /ɪnˈfekʃəs/, protective /prəˈtektɪv/ nhấn âm 2; elegant /ˈelɪɡənt/ nhấn âm 1. Chọn <b>elegant</b>.')
SND('pa2', '2324', 'limit|obey|forbid|impose', 'A', 'limit /ˈlɪmɪt/ nhấn âm 1; obey /əˈbeɪ/, forbid /fəˈbɪd/, impose /ɪmˈpəʊz/ nhấn âm 2. Chọn <b>limit</b>.')
SND('pa2', '2324', 'design|model|future|question', 'A', 'design /dɪˈzaɪn/ nhấn âm 2; model /ˈmɒdl/, future /ˈfjuːtʃə/, question /ˈkwestʃən/ nhấn âm 1. Chọn <b>design</b>.')
SND('pa2', '2324', 'impress|install|begin|sensor', 'D', 'impress /ɪmˈpres/, install /ɪnˈstɔːl/, begin /bɪˈɡɪn/ nhấn âm 2; sensor /ˈsensə/ nhấn âm 1. Chọn <b>sensor</b>.')
SND('pa2', '2324', 'solution|camera|effective|electric', 'B', 'solution /səˈluːʃn/, effective /ɪˈfektɪv/, electric /ɪˈlektrɪk/ nhấn âm 2; camera /ˈkæmərə/ nhấn âm 1. Chọn <b>camera</b>.')
SND('pa2', '2324', 'negative|vehicle|pollution|operate', 'C', 'negative /ˈneɡətɪv/, vehicle /ˈviːəkl/, operate /ˈɒpəreɪt/ nhấn âm 1; pollution /pəˈluːʃn/ nhấn âm 2. Chọn <b>pollution</b>.')
SND('pa2', '2324', 'efficiently|sustainable|pedestrian|vegetable', 'D', 'efficiently /ɪˈfɪʃntli/, sustainable /səˈsteɪnəbl/, pedestrian /pəˈdestriən/ nhấn âm 2; vegetable /ˈvedʒtəbl/ nhấn âm 1. Chọn <b>vegetable</b>.')
SND('pa2', '2324', 'activity|information|technology|convenient', 'B', 'activity /ækˈtɪvəti/, technology /tekˈnɒlədʒi/, convenient /kənˈviːniənt/ nhấn âm 2; information /ˌɪnfəˈmeɪʃn/ nhấn âm 3. Chọn <b>information</b>.')
SND('pa2', '2425', 'follow|gender|footstep|belief', 'D', 'follow /ˈfɒləʊ/, gender /ˈdʒendə/, footstep /ˈfʊtstep/ nhấn âm 1; belief /bɪˈliːf/ nhấn âm 2. Chọn <b>belief</b>.')
SND('pa2', '2425', 'behave|differ|argue|follow', 'A', 'behave /bɪˈheɪv/ nhấn âm 2; differ /ˈdɪfə/, argue /ˈɑːɡjuː/, follow /ˈfɒləʊ/ nhấn âm 1. Chọn <b>behave</b>.')
SND('pa2', '2425', 'healthy|problem|mental|amount', 'D', 'amount /əˈmaʊnt/ nhấn âm 2; healthy /ˈhelθi/, problem /ˈprɒbləm/, mental /ˈmentl/ nhấn âm 1. Chọn <b>amount</b>.')
SND('pa2', '2425', 'lifestyle|frequent|complain|balance', 'C', 'complain /kəmˈpleɪn/ nhấn âm 2; lifestyle /ˈlaɪfstaɪl/, frequent /ˈfriːkwənt/, balance /ˈbæləns/ nhấn âm 1. Chọn <b>complain</b>.')
SND('pa2', '2425', 'technology|environment|economy|architecture', 'D', 'technology /tekˈnɒlədʒi/, environment /ɪnˈvaɪrənmənt/, economy /ɪˈkɒnəmi/ nhấn âm 2; architecture /ˈɑːkɪtektʃə/ nhấn âm 1. Chọn <b>architecture</b>.')
SND('pa2', '2425', 'population|operation|infrastructure|exhibition', 'C', 'population /ˌpɒpjuˈleɪʃn/, operation /ˌɒpəˈreɪʃn/, exhibition /ˌeksɪˈbɪʃn/ nhấn âm 3 (trước -tion); infrastructure /ˈɪnfrəstrʌktʃə/ nhấn âm 1. Chọn <b>infrastructure</b>.')
SND('pa2', '2425', 'device|complain|limit|allow', 'C', 'device /dɪˈvaɪs/, complain /kəmˈpleɪn/, allow /əˈlaʊ/ nhấn âm 2; limit /ˈlɪmɪt/ nhấn âm 1. Chọn <b>limit</b>.')
SND('pa2', '2425', 'teenager|computer|conclusion|supporting', 'A', 'teenager /ˈtiːneɪdʒə/ nhấn âm 1; computer /kəmˈpjuːtə/, conclusion /kənˈkluːʒn/, supporting /səˈpɔːtɪŋ/ nhấn âm 2. Chọn <b>teenager</b>.')

# ======================================================================================
# TỪ VỰNG
# ======================================================================================
# ---- tv1: chọn từ / cụm từ / giới từ / dạng từ
M('tv1', '2223', 'My grandpa is the most conservative person in my family. He never ______ about his way of life.', 'gives his opinion|changes his mind|gives his view|keeps in mind', 'B', 'conservative (bảo thủ) → ông không bao giờ <b>change his mind</b> (thay đổi ý kiến) về lối sống. Các phương án còn lại không hợp nghĩa "bảo thủ".')
M('tv1', '2223', 'Teens should have the ability to ______ loneliness.', 'deal|cope with|set up|look after', 'B', '<b>cope with</b> = đối phó/vượt qua. "deal" phải đi với "with" (deal with); set up = thành lập; look after = chăm sóc.')
M('tv1', '2223', 'Being ______ means you will not ask parents for help whenever there is a problem.', 'reliable|protective|humanitarian|self-reliant', 'D', '<b>self-reliant</b> = tự lực, không dựa dẫm. reliable = đáng tin cậy; protective = hay bảo vệ; humanitarian = nhân đạo.')
M('tv1', '2223', 'Our team needs a ______ leader who can make important decisions quickly and confidently.', 'decisive|reliable|independent|determined', 'A', '<b>decisive</b> = quyết đoán (đưa ra quyết định nhanh, tự tin).')
M('tv1', '2223', 'Their close friendship ______ a romantic relationship.', 'brings about|puts up|takes over|turns into', 'D', '<b>turn into</b> = biến thành. bring about = gây ra; put up = dựng lên; take over = tiếp quản.')
M('tv1', '2223', 'When Laura suffered a break-up in her relationship, she saw a/an ______ for advice.', 'assistant|counselor|agency|service', 'B', '<b>counselor</b> = chuyên viên tư vấn → đi gặp để xin lời khuyên.')
M('tv1', '2223', 'Teenagers ought to live ______. It is impossible to rely on their parents all the time.', 'independently|independent|independence|dependently', 'A', 'Sau động từ "live" cần trạng từ: <b>independently</b> (một cách độc lập).')
M('tv1', '2223', 'Members of 4 generations in his family produce furniture so his parents want him to ______ in their footsteps.', 'follow|watch|observe|work', 'A', 'Thành ngữ <b>follow in someone\'s footsteps</b> = nối nghiệp, theo bước chân ai.')
M('tv1', '2223', 'Online ______ services have helped lots of single people to find future husbands or wives.', 'date|dating|dated|dates', 'B', '<b>dating services</b> = dịch vụ hẹn hò (danh từ ghép: V-ing + N).')
M('tv1', '2223', 'When people live in an extended family, there is often a ______.', 'generation gap|viewpoint|independence|housework', 'A', 'Sống chung nhiều thế hệ thường có <b>generation gap</b> (khoảng cách thế hệ).')
M('tv1', '2223', 'They were finally ______ with each other, after not speaking for nearly five years.', 'reconciled|persuaded|interested|fond', 'A', '<b>be reconciled with</b> = làm lành/hòa giải với nhau.')
M('tv1', '2223', 'Parents are willing to lend a sympathetic ______ to their children when they have problems.', 'eye|hand|ear|paw', 'C', 'Thành ngữ <b>lend a sympathetic ear</b> = lắng nghe một cách thông cảm.')
M('tv1', '2223', 'She can make friends easily because she has good ______ skills.', 'interpersonal communication|time management|housekeeping|problem solving', 'A', 'Kết bạn dễ dàng → kỹ năng <b>giao tiếp liên cá nhân</b> (interpersonal communication).')
M('tv1', '2223', '______ education refers to both classes and schools that have students of only one gender.', 'Vocational|Single-sex|Home|Further', 'B', '<b>Single-sex education</b> = giáo dục đơn giới (chỉ nam hoặc chỉ nữ).')
M('tv1', '2223', 'One negative effect of having a romantic relationship is that you might not ______ on your study.', 'depend|experiment|concentrate|insist', 'C', '<b>concentrate on</b> = tập trung vào. depend on / insist on có nghĩa khác.')
M('tv1', '2223', 'Teenagers tend to spend more time ______ with their peers than with their parents.', 'judging|obeying|forbiding|interacting', 'D', '<b>interact with</b> = tương tác với bạn bè đồng trang lứa (peers).')
# 2324 – Unit 1
M('tv1', '2324', 'I like working ______ in the gym.', 'up|on|over|out', 'D', '<b>work out</b> = tập thể dục.')
M('tv1', '2324', 'Watching too much television is not good ______ your eyes.', 'at|for|with|to', 'B', '<b>be good for</b> = tốt cho.')
M('tv1', '2324', 'About 50,000 bicyclists suffer ______ serious head injuries each year.', 'on|from|at|about', 'B', '<b>suffer from</b> = chịu đựng/bị (bệnh, chấn thương).')
M('tv1', '2324', 'Some can cause ______ diseases such as tuberculosis and food poisoning.', 'infect|infection|infectious|infectiously', 'C', 'Trước danh từ "diseases" cần tính từ: <b>infectious diseases</b> (bệnh truyền nhiễm).')
M('tv1', '2324', 'Remember that even simple ______ changes can boost our immune system.', 'diet|dietary|dieting|diets', 'B', 'Cần tính từ bổ nghĩa cho "changes": <b>dietary changes</b> (thay đổi trong chế độ ăn).')
M('tv1', '2324', 'Seasonal vaccines are used to protect against ______ viruses.', 'differ|different|differently|difference', 'B', 'Tính từ đứng trước danh từ: <b>different viruses</b>.')
M('tv1', '2324', 'Vaccines are often used to prevent the ______ of diseases caused by viruses.', 'development|increase|decrease|spread', 'D', '<b>prevent the spread of diseases</b> = ngăn chặn sự lây lan của bệnh.')
M('tv1', '2324', 'The smallest ______ are about 0.4 micron in diameter.', 'animals|species|bacteria|diseases', 'C', 'Vật nhỏ cỡ 0,4 micron là <b>bacteria</b> (vi khuẩn).')
M('tv1', '2324', 'Start by looking at food labels, paying attention to ingredients and ______ such as vitamins and minerals.', 'nutrients|features|types|drinkables', 'A', 'Vitamins và minerals là các <b>nutrients</b> (chất dinh dưỡng).')
M('tv1', '2324', 'The screens ______ blue light that can prevent you from sleeping well.', 'give away|give out|give in|give off', 'D', '<b>give off</b> = phát ra (ánh sáng, mùi, nhiệt). give out = phân phát; give in = nhượng bộ.')
M('tv1', '2324', 'Living in a/an ______ will provide you immense delight and the support of family members from many generations.', 'nuclear family|extended family|traditional family|close family', 'B', 'Nhiều thế hệ sống chung = <b>extended family</b> (gia đình nhiều thế hệ).')
M('tv1', '2324', 'To stay healthy, you need to ______ for at least 30 minutes a day.', 'run out|run on|work on|work out', 'D', '<b>work out</b> = tập luyện. run out = hết; work on = nỗ lực làm.')
# 2324 – Unit 2
M('tv1', '2324', 'I was tired and couldn\'t concentrate ______ doing my research project properly.', 'on|in|of|for', 'A', '<b>concentrate on</b> + V-ing.')
M('tv1', '2324', 'Parents can\'t always respond effectively to aggressive ______ of their children.', 'behaved|behaving|behaviour|behave', 'C', 'Sau tính từ "aggressive" cần danh từ: <b>aggressive behaviour</b> (hành vi hung hăng).')
M('tv1', '2324', 'She lives with grandparents who have ______ views.', 'tradition|traditional|traditionally|traditionalize', 'B', 'Tính từ bổ nghĩa cho "views": <b>traditional views</b> (quan điểm truyền thống).')
M('tv1', '2324', 'My parents always complain ______ my clothes and hairstyle.', 'about|in|of|for', 'A', '<b>complain about</b> = phàn nàn về.')
M('tv1', '2324', 'Bob used to completely rely ______ his parents.', 'in|for|on|with', 'C', '<b>rely on</b> = dựa vào.')
M('tv1', '2324', 'His ______ in God gave him hope during difficult times.', 'believe|believable|believably|belief', 'D', 'Sau "His" cần danh từ: <b>belief</b> (niềm tin).')
M('tv1', '2324', 'Lots of teenagers are so stubborn and refuse to ______ their parents\' advice.', 'receive|bring|follow|regard', 'C', '<b>follow advice</b> = nghe theo lời khuyên.')
M('tv1', '2324', 'Living in three- or four-generational families, commonly referred to as "______ families", has both benefits and drawbacks.', 'single-parent|extended|nuclear|crowded', 'B', '<b>extended families</b> = gia đình nhiều thế hệ.')
M('tv1', '2324', 'Four generations living under the same roof will have different ______ of lifestyle.', 'gaps|rules|manners|viewpoints', 'D', '<b>different viewpoints of lifestyle</b> = những quan điểm khác nhau về lối sống.')
M('tv1', '2324', 'After graduating from university, I want to ______ my father\'s footsteps.', 'follow in|succeed in|go after|keep up', 'A', '<b>follow in someone\'s footsteps</b> = nối nghiệp ai.')
M('tv1', '2324', 'Gen Zers are very ______ as they always come up with new ideas or things.', 'experienced|curious|creative|traditional', 'C', 'Luôn nghĩ ra ý tưởng mới → <b>creative</b> (sáng tạo).')
M('tv1', '2324', 'Older generations often have very ______ about how people should live.', 'common characteristics|traditional views|generational conflicts|cultural values', 'B', '<b>traditional views</b> = quan điểm truyền thống về cách sống.')
M('tv1', '2324', 'We should respect the ______ that have been passed down from the previous generations.', 'family conflicts|generational differences|cultural values|common behaviours', 'C', 'Những thứ được truyền lại qua các thế hệ → <b>cultural values</b> (giá trị văn hoá).')
# 2324 – Unit 3
M('tv1', '2324', 'The cities of the future will be ______ thanks to green technologies.', 'sustain|sustainable|sustainability|sustainably', 'B', 'Sau "will be" cần tính từ: <b>sustainable</b> (bền vững).')
M('tv1', '2324', 'Smart devices help cities operate more ______.', 'effect|effective|effectively|effected', 'C', 'Bổ nghĩa cho động từ "operate" cần trạng từ: <b>effectively</b>.')
M('tv1', '2324', 'Using public transport will help reduce traffic jams and ______.', 'pollute|polluted|pollution|to pollute', 'C', 'Song song với danh từ "traffic jams" → danh từ <b>pollution</b>.')
M('tv1', '2324', 'Eco-friendly transport systems will reduce greenhouse gas ______.', 'emit|emitted|emissions|to emit', 'C', '<b>greenhouse gas emissions</b> = khí thải nhà kính.')
M('tv1', '2324', 'More than fifty percent of the green city is made up ______ green areas.', 'on|from|of|for', 'C', '<b>be made up of</b> = được tạo thành từ.')
M('tv1', '2324', 'It seems a good solution ______ many environmental problems.', 'for|to|of|in', 'B', '<b>a solution to</b> + vấn đề.')
M('tv1', '2324', 'Local authorities should find ways to limit the use of private cars and encourage city ______ to use public transport.', 'commuters|planners|dwellers|people', 'C', '<b>city dwellers</b> = người dân thành phố (từ vựng Unit 3). "commuters" cũng có thể chấp nhận.')
N('tv1 (2324 U3 #19 "city ___ to use public transport"): city dwellers (C) và city commuters (A) đều hợp lý → chấp nhận cả A, C.')
M('tv1', '2324', 'The new underground has allowed city dwellers to ______ more easily.', 'make up|get round|get out|move away', 'B', '<b>get round</b> = đi lại, di chuyển quanh thành phố.')
M('tv1', '2324', 'In developing countries people are ______ overcrowded cities in great numbers.', 'breaking down|filling up|pouring into|paying for', 'C', '<b>pour into</b> = đổ xô vào (số lượng lớn).')
M('tv1', '2324', 'There are other problems of city life which I don\'t propose to ______ at the moment.', 'go into|go around|go for|go up', 'A', '<b>go into</b> = đi sâu vào, bàn kỹ về.')
M('tv1', '2324', 'Cities in poorer countries often lack basic ______. Without it, they are unable to function properly as cities.', 'structure|construction|infrastructure|condition', 'C', '<b>infrastructure</b> = cơ sở hạ tầng.')
M('tv1', '2324', 'We will need new technologies to generate ______ energy and use it in clean and safe ways.', 'liveable|controlled|renewable|endurable', 'C', '<b>renewable energy</b> = năng lượng tái tạo.')
# tn
M('tv1', 'tn', 'Women have a longer life ______ than men.', 'story|membership|history|expectancy', 'D', '<b>life expectancy</b> = tuổi thọ trung bình.')
M('tv1', 'tn', 'You should continue to lead a healthy life, such as eating a(n) ______ diet, taking exercise and keeping warm.', 'balanced|sensitive|poor|unhealthy', 'A', '<b>balanced diet</b> = chế độ ăn cân bằng (hợp với "healthy life").')
M('tv1', 'tn', 'It\'s a good idea to stretch your ______ after weight lifting.', 'power|muscles|strength|movements', 'B', '<b>stretch your muscles</b> = giãn cơ.')
M('tv1', 'tn', 'Phong works ______ in the gym two or three times a week.', 'off|over|against|out', 'D', '<b>work out</b> = tập thể dục.')
M('tv1', 'tn', 'The building has many features that make it more ______ as well as reducing heating costs.', 'eco-friendly|ecological|economic|ecologically', 'A', '<b>eco-friendly</b> = thân thiện với môi trường (tính từ sau "more").')
M('tv1', 'tn', 'Our city has recently been voted one of the most ______ towns in the country.', 'living|lively|livable|live', 'C', '<b>livable</b> = đáng sống.')
M('tv1', 'tn', 'Chemotherapy is the most common treatment ______ cancer.', 'about|with|of|to', 'C', '<b>treatment of cancer</b> = điều trị ung thư. (Phương án "for" không có trong đề; "of" là đáp án phù hợp nhất.)')
N('tv1 (tn "treatment ___ cancer"): cụm chuẩn là "treatment for/of cancer"; đề không có "for" → chọn of (C).')
M('tv1', 'tn', 'Optimistic people believe that city ______ will have a better life thanks to important achievements in technology and medicine.', 'citizens|locals|dwellers|occupants', 'C', '<b>city dwellers</b> = cư dân thành phố (collocation cố định). citizens cũng gặp nhưng "city dwellers" là từ Unit 3.')
M('tv1', 'tn', 'Cities in poorer countries often lack basic ______. Without it, they are unable to function properly as cities.', 'structure|construction|infrastructure|condition', 'C', '<b>infrastructure</b> = cơ sở hạ tầng.')
M('tv1', 'tn', 'Many teenagers do not like it when their parents impose their decision ______ them.', 'in|on|at|to', 'B', '<b>impose something on someone</b> = áp đặt cho ai.')
M('tv1', 'tn', 'Lots of teenagers are so stubborn and refuse to ______ their parents\' advice.', 'receive|bring|follow|regard', 'C', '<b>follow advice</b> = nghe theo lời khuyên.')
M('tv1', 'tn', 'Exercise ______ to always keep your body fit and your mind happy.', 'regular|regularly|irregular|irregularly', 'B', 'Bổ nghĩa cho động từ "exercise" cần trạng từ <b>regularly</b> (tập luyện đều đặn).')
# 2425
M('tv1', '2425', 'The ______ arises when Jack and his parents have considerable disagreement on his choice of university.', 'discrimination|conflict|agreement|gap', 'B', '<b>conflict</b> = mâu thuẫn, xung đột (do bất đồng).')
M('tv1', '2425', 'She doesn\'t want to waste her money on clothes, so she ignores the ______ fashion trend.', 'comfortable|current|Mature|stylish', 'B', '<b>current fashion trend</b> = xu hướng thời trang hiện nay.')
M('tv1', '2425', 'When you ride a motorbike, you must ______ the general road rules.', 'judge|force|obey|conform', 'C', '<b>obey the rules</b> = tuân thủ luật. "conform" cần giới từ "to".')
M('tv1', '2425', 'Instead of ______ someone by their appearance, you should get to know them better.', 'swearing|judging|controlling|viewing', 'B', '<b>judge someone by their appearance</b> = đánh giá ai qua vẻ bề ngoài.')
M('tv1', '2425', 'Having two children in a family is becoming the ______ in some Asian countries.', 'norm|privacy|conflict|behavior', 'A', '<b>the norm</b> = chuẩn mực, điều phổ biến.')
M('tv1', '2425', 'My parents do not want me to wear ______ dresses because they think that they aren\'t suitable for my age.', 'tight|casual|rude|sporty', 'A', 'Cha mẹ cho rằng không hợp lứa tuổi → váy <b>tight</b> (bó sát) là hợp lý nhất.')
M('tv1', '2425', 'I don\'t understand why you like ______ clothes. They are too bright and young for your age.', 'flashy|fashionable|comfortable|stylish', 'A', '<b>flashy</b> = loè loẹt, quá sặc sỡ.')
M('tv1', '2425', 'We should develop such ______ sources of energy as solar energy and nuclear energy.', 'tradition|alternative|revolutionary|surprising', 'B', '<b>alternative sources of energy</b> = nguồn năng lượng thay thế.')
M('tv1', '2425', 'City ______ can enjoy better health care than people living in the countryside, but they are usually busier and more stressed because of the city\'s fast pace of life.', 'dwellers|inhabitants|infrastructure|ancestors', 'A', '<b>city dwellers</b> = cư dân thành phố ("inhabitants" thường dùng với "of + địa danh").')
M('tv1', '2425', 'London won\'t be a good place to live, will it? – ______ it will be.', 'On the contrary|As the contrary|On contrary|On contrast', 'A', 'Cụm cố định: <b>On the contrary</b> = trái lại (phủ nhận ý câu trước).')
M('tv1', '2425', 'Cities in the future will also be sustainable. They will include a lot of green space and become ______ to more plants and animals.', 'house|home|housing|dwelling', 'B', '<b>become home to</b> = trở thành nơi sinh sống của.')
M('tv1', '2425', 'Constant ______ of attack makes everyday life dangerous here.', 'threat|threaten|threatening|threateningly', 'A', 'Sau "Constant" cần danh từ: <b>threat of attack</b> = nguy cơ bị tấn công.')
M('tv1', '2425', 'The instructions give a balanced ______ and protect against infections.', 'physic|treatment|diet|injury', 'C', '<b>a balanced diet</b> = chế độ ăn cân bằng.')
M('tv1', '2425', 'She suffers ______ a rare bone disease.', 'to|about|on|from', 'D', '<b>suffer from</b> + bệnh.')
M('tv1', '2425', 'You can change your eating habits and lead a healthier ______.', 'health|develop|lifestyle|muscles', 'C', '<b>lead a healthier lifestyle</b> = sống lành mạnh hơn.')
M('tv1', '2425', 'Viruses can cause a range of illness, from the common cold or the flu to more ______ diseases such as AIDS and Covid-19.', 'infectious|minimal|serious|benign', 'C', '"more ... diseases" so với cảm lạnh → bệnh <b>serious</b> (nghiêm trọng) hơn.')
M('tv1', '2425', 'Baking soda is considered the best home ______ for acne as it soothes itching and inflammation around spots.', 'chemical|medicine|remedy|substance', 'C', '<b>home remedy</b> = bài thuốc/phương pháp chữa tại nhà.')
M('tv1', '2425', 'I have maintained a healthy lifestyle recently. Therefore, I avoided the unpleasant experience of food ______.', 'poisonous|poison|poisoning|poisonousness', 'C', '<b>food poisoning</b> = ngộ độc thực phẩm.')
M('tv1', '2425', 'Generations often ______ social values and norms, reflecting the difference of perspectives.', 'argue over|bond over|make over|push over', 'A', '<b>argue over</b> = tranh cãi về → phản ánh khác biệt quan điểm. bond over = gắn kết nhờ.')
M('tv1', '2425', 'Linh lives in a/an ______ family. It has 3 generations: her grandparents, her parents and she.', 'nuclear|small|affected|extended', 'D', '3 thế hệ sống chung = <b>extended family</b>.')
M('tv1', '2425', 'Exhaust ______ from cars are responsible for much of the air pollution in cities.', 'fumes|smokes|gases|smog', 'A', '<b>exhaust fumes</b> = khí thải/khói xả của xe.')
M('tv1', '2425', 'Luckily, my parents are always willing to listen to my new ideas. They\'re very ______.', 'narrow-minded|open-minded|elegant|careful', 'B', 'Sẵn sàng nghe ý tưởng mới → <b>open-minded</b> (cởi mở).')
M('tv1', '2425', 'Vaccines are often used to prevent the ______ of diseases caused by viruses.', 'development|increase|decrease|spread', 'D', '<b>prevent the spread of</b> = ngăn sự lây lan của.')

# ---- tv2: đồng nghĩa
M('tv2', '2223', 'Some parents strongly <u>oppose</u> their children\'s romantic relationship.', 'assist|forbid|ignore|preserve', 'B', '<b>oppose</b> = phản đối ≈ <b>forbid</b> (cấm đoán). assist = giúp; ignore = phớt lờ; preserve = bảo tồn.')
M('tv2', '2223', 'I\'m totally exhausted after having finished successive <u>assignments</u> in only a week.', 'Jobs|works|exercises|problems', 'C', '<b>assignments</b> = bài tập/nhiệm vụ được giao ≈ <b>exercises</b>.')
M('tv2', '2223', 'He is truly a <u>reliable</u> friend. He will always be with me and never let me down.', 'mean|independent|decisive|dependable', 'D', '<b>reliable</b> = đáng tin cậy ≈ <b>dependable</b>.')
M('tv2', '2223', 'In spite of poverty and dreadful conditions, they still manage to keep their <u>self-respect</u>.', 'self-reliant|self-restraint|self-esteem|self-assured', 'C', '<b>self-respect</b> = lòng tự trọng ≈ <b>self-esteem</b>.')
M('tv2', '2324', 'You should also <u>exercise</u> in the early morning when the weather is not too hot.', 'have a rest|do housework|do homework|work out', 'D', '<b>exercise</b> = tập thể dục ≈ <b>work out</b>.')
M('tv2', '2324', 'In Vietnam, <u>life expectancy</u> for both men and women has increased significantly over the last ten years.', 'living standard|longevity|life skill|lifeline', 'B', '<b>life expectancy</b> = tuổi thọ ≈ <b>longevity</b>.')
M('tv2', '2324', '<u>Obesity</u> and heart disease can be exacerbated by excessive fast-food consumption.', 'Being underweight|Being overweight|Child malnutrition|Famine stricken', 'B', '<b>obesity</b> = béo phì ≈ <b>being overweight</b>.')
M('tv2', '2324', 'They give us advice, but never <u>force</u> us to follow in their footsteps.', 'ask|advise|warn|oblige', 'D', '<b>force</b> = ép buộc ≈ <b>oblige</b> (bắt buộc).')
M('tv2', '2324', 'They <u>experienced</u> many social changes and developments in history.', 'went through|looked up|came into|gave off', 'A', '<b>experience</b> = trải qua ≈ <b>go through</b>.')
M('tv2', '2324', 'My parents need to <u>hire</u> someone to look after my grandparents.', 'employ|lend|borrow|invite', 'A', '<b>hire</b> = thuê ≈ <b>employ</b>.')
M('tv2', '2324', 'Sorghum is a brand new cash crop that can be burned as a fuel and is therefore a <u>renewable</u> source of energy.', 'inexhaustible|recyclable|green|adverse', 'A', '<b>renewable</b> = tái tạo được ≈ <b>inexhaustible</b> (không bao giờ cạn).')
M('tv2', '2324', 'The wind farm may be able to <u>generate</u> enough electricity for 2,000 homes.', 'afford|produce|design|install', 'B', '<b>generate</b> = tạo ra ≈ <b>produce</b>.')
M('tv2', '2324', 'Many organizations have been <u>involved in</u> drawing up the report on environmental campaigns.', 'concerned about|confined in|enquired about|engaged in', 'D', '<b>be involved in</b> = tham gia ≈ <b>be engaged in</b>.')
M('tv2', 'tn', 'This kind of fruit helps to <u>boost</u> the immune system.', 'decrease|reduce|increase|maintain', 'C', '<b>boost</b> = tăng cường ≈ <b>increase</b>.')
M('tv2', 'tn', 'In Vietnam, <u>life expectancy</u> for both men and women has increased significantly over the last ten years.', 'living standard|longevity|life skills|lifeline', 'B', '<b>life expectancy</b> ≈ <b>longevity</b>.')
M('tv2', '2425', 'They hope that these energy resources will <u>step by step</u> replace fossil fuels such as gas, coal, and oil in the next twenty years.', 'gradually|slower and slower|faster and faster|A & B', 'A', '<b>step by step</b> = từng bước ≈ <b>gradually</b> (dần dần).')

# ---- tv3: trái nghĩa
M('tv3', '2223', 'The maintenance of this company is <u>dependent on</u> international investment.', 'affective|self-reliant|self-restricted|reliant', 'B', '<b>dependent on</b> (phụ thuộc vào) ↔ <b>self-reliant</b> (tự lực).')
M('tv3', '2223', 'I was really <u>depressed</u> about his winning the election, like a lot of people.', 'fed up|pessimistic|satisfied|unhappy', 'C', '<b>depressed</b> (chán nản) ↔ <b>satisfied</b> (hài lòng).')
M('tv3', '2223', 'Nam is considered to be the best student in our class because he\'s not only good at learning but also <u>well-informed</u> about everything around the world.', 'perfectly-informed|badly-informed|bad-informed|ill-informed', ['B', 'D'], '<b>well-informed</b> (am hiểu) ↔ <b>ill-informed / badly-informed</b> (thiếu hiểu biết). "bad-informed" sai ngữ pháp.')
N('tv3 (2223 well-informed): ill-informed (D) là từ chuẩn, badly-informed (B) cũng được dùng → chấp nhận B, D.')
M('tv3', '2223', 'Jane found herself in <u>conflict</u> with her parents over her future career.', 'disagreement|harmony|controversy|fighting', 'B', '<b>conflict</b> (xung đột) ↔ <b>harmony</b> (hòa thuận).')
M('tv3', '2324', 'I discovered a website that advertised a quick and easy way to <u>lose</u> weight in one month.', 'suffer|treat|maintain|gain', 'D', '<b>lose weight</b> ↔ <b>gain weight</b> (tăng cân).')
M('tv3', '2324', 'Before you begin your yoga practice, you should do some warm-up exercises such as <u>stretching</u>.', 'remaining|maintaining|performing|shrinking', 'D', '<b>stretch</b> (giãn ra) ↔ <b>shrink</b> (co lại).')
M('tv3', '2324', 'Don\'t look down at your feet as you walk. This will cause you to slow down and <u>cause</u> back pain.', 'result in|result from|lead to|give off', 'B', '<b>cause</b> (gây ra) ↔ <b>result from</b> (là do/kết quả của). result in và lead to đồng nghĩa với cause.')
M('tv3', '2324', 'Having an <u>extended family</u>, however, did not always guarantee a role.', 'close family|traditional family|nuclear family|large family', 'C', '<b>extended family</b> (gia đình nhiều thế hệ) ↔ <b>nuclear family</b> (gia đình hạt nhân: bố mẹ và con).')
M('tv3', '2324', 'Jane found herself in <u>conflict</u> with her parents over her future career.', 'disagreement|harmony|controversy|combat', 'B', '<b>conflict</b> ↔ <b>harmony</b>.')
M('tv3', '2324', 'My children\'s noise is interfering with my ability to <u>concentrate</u> on my work.', 'focus|abandon|neglect|permit', 'C', '<b>concentrate</b> (tập trung) ↔ <b>neglect</b> (lơ là, không chú ý). focus là đồng nghĩa.')
N('tv3 (2324 U2 #19 concentrate): phương án thấy trong nguồn bị tách dòng (A focus, B abandon, C neglect, D permit) – chọn neglect (C), hơi mơ hồ.')
M('tv3', '2324', 'People who live in towns and cities live in an <u>urban</u> environment.', 'remote|convenient|suburban|rural', 'D', '<b>urban</b> (đô thị) ↔ <b>rural</b> (nông thôn).')
M('tv3', '2324', 'We need to do more to make the neighborhood safer and more <u>livable</u>.', 'inhabitable|uninhabitable|dangerous|prosperous', 'B', '<b>livable</b> (đáng sống) ↔ <b>uninhabitable</b> (không thể sống được).')
M('tv3', '2324', 'You can\'t <u>neglect</u> your study because the exam is coming soon.', 'call on|give off|focus on|carry out', 'C', '<b>neglect</b> (bỏ bê) ↔ <b>focus on</b> (tập trung vào).')
M('tv3', 'tn', 'Having an <u>extended family</u>, however, did not always guarantee a role.', 'close family|traditional family|nuclear family|large family', 'C', '<b>extended family</b> ↔ <b>nuclear family</b> (gia đình hạt nhân).')
M('tv3', 'tn', 'Jane found herself in <u>conflict</u> with her parents over her future career.', 'disagreement|harmony|controversy|combat', 'B', '<b>conflict</b> ↔ <b>harmony</b>.')
M('tv3', 'tn', 'The basic challenge for <u>sustainable</u> agriculture is to maximise the use of locally available and renewable resources.', 'long-term|short-term|beneficial|harmful', 'B', '<b>sustainable</b> (bền vững, lâu dài) ↔ <b>short-term</b> (ngắn hạn).')

# ---- tv4: dạng từ (tn B. TỰ LUẬN + 2425 Q41,43)
F('tv4', 'tn', 'Born and raised in America, John celebrates and values {_}.', ['individuality', 'individualism'], 'Sau động từ "values" cần danh từ: <b>individuality</b> (cá tính, tính cá nhân) – hoặc individualism (chủ nghĩa cá nhân).', hint='INDIVIDUAL')
F('tv4', 'tn', 'Future cities will use {_} energy in order to be sustainable.', ['renewable'], 'Tính từ bổ nghĩa cho "energy": <b>renewable</b> (tái tạo).', hint='RENEW')
F('tv4', 'tn', 'Those who were born and grew up in the era of technology are called {_} natives.', ['digital'], '<b>digital natives</b> = thế hệ sinh ra trong thời đại số.', hint='DIGIT')
F('tv4', 'tn', 'There are at least three {_} living under the same roof in my family.', ['generations'], 'Sau "three" cần danh từ số nhiều: <b>generations</b> (thế hệ).', hint='GENERATIONAL')
F('tv4', 'tn', 'The elderly are more {_} about their eating habit.', ['conservative'], 'Sau "are more" cần tính từ: <b>conservative</b> (bảo thủ, thận trọng).', hint='CONSERVATIVELY')
F('tv4', 'tn', 'Just taking vitamin tablets will not turn an {_} diet into a good one.', ['unhealthy'], 'Tính từ trước "diet" và trái nghĩa với "good": <b>unhealthy</b> (không lành mạnh).', hint='HEALTH')
F('tv4', 'tn', 'Life {_} for both men and women has improved greatly in the past 20 years.', ['expectancy'], '<b>life expectancy</b> = tuổi thọ trung bình.', hint='EXPECT')
F('tv4', 'tn', 'The virus affects the body\'s immune system so that it cannot fight {_}.', ['infection', 'infections'], 'Sau động từ "fight" cần danh từ: <b>infection</b> (sự nhiễm trùng).', hint='INFECT')
F('tv4', '2425', 'My darling, you looked {_} in that dress.', ['beautiful', 'beautifully'], 'Sau linking verb "looked" cần tính từ: <b>beautiful</b>.', hint='beauty')
F('tv4', '2425', 'After a long time working incessantly, all my efforts ended in {_}.', ['success'], 'Sau giới từ "in" cần danh từ: <b>success</b> (thành công).', hint='succeed')

# ======================================================================================
# NGỮ PHÁP
# ======================================================================================
# ---- ng1: quá khứ đơn / hiện tại hoàn thành
M('ng1', '2324', 'I haven\'t met him again since we ______ school ten years ago.', 'have left|leave|left|had left', 'C', 'Mệnh đề sau <b>since</b> chỉ mốc thời gian trong quá khứ ("ten years ago") → dùng quá khứ đơn: <b>left</b>. Cấu trúc: S + have/has + V3 + since + S + V2.')
M('ng1', '2324', 'We ______ them since we left school.', 'don\'t meet|haven\'t met|hasn\'t met|didn\'t meet', 'B', 'Có <b>since + mốc quá khứ</b> → hiện tại hoàn thành; chủ ngữ "We" → <b>haven\'t met</b>.')
M('ng1', '2324', 'My father ______ late at work this month. He feels exhausted.', 'is staying|stayed|has stayed|will stay', 'C', '<b>this month</b> (khoảng thời gian chưa kết thúc) và kết quả ở hiện tại ("feels exhausted") → hiện tại hoàn thành: <b>has stayed</b>.')
M('ng1', '2324', 'She ______ two miles and a half, and now she feels exhausted.', 'will have run|was running|has run|ran', 'C', 'Hành động vừa xong, kết quả còn ở hiện tại ("now she feels exhausted") → <b>has run</b>.')
M('ng1', 'tn', 'We ______ since we left school.', 'don\'t meet|haven\'t met|hasn\'t met|didn\'t meet', 'B', 'since + mốc quá khứ → hiện tại hoàn thành, chủ ngữ số nhiều: <b>haven\'t met</b>.')
M('ng1', '2425', 'We ______ touch since we ______ school three years ago.', 'were losing/had left|lost/ have left|have lost/ left|have lost / leave', 'C', 'Vế trước "since": hiện tại hoàn thành (<b>have lost</b> touch); vế sau "since" có "three years ago" → quá khứ đơn <b>left</b>.')
M('ng1', '2425', 'My parents first ______ each other at the Olympic Games in 1982.', 'had met|met|have met|meet', 'B', 'Mốc thời gian xác định trong quá khứ (<b>in 1982</b>) → quá khứ đơn: <b>met</b>.')
M('ng1', '2425', 'Since Lan moved to Paris, I ______ anything from her.', 'didn\'t hear|haven\'t heard|don\'t hear|wasn\'t hearing', 'B', '<b>Since + mệnh đề quá khứ đơn</b> → mệnh đề chính dùng hiện tại hoàn thành: <b>haven\'t heard</b>.')
M('ng1', '2425', 'My sister was listening to music while my brother ______ video games.', 'played|has played|was watching|had played', 'A', 'Hai hành động xảy ra song song trong quá khứ; vế "was listening … while" → quá khứ tiếp diễn hoặc quá khứ đơn. Trong các phương án chỉ <b>played</b> hợp ngữ pháp và nghĩa ("was watching video games" không hợp).')
N('ng1 (2425 Ex3 #26): đáp án lý tưởng là "was playing"; đề không có → chọn played (A).')

# ---- ng2: động từ khuyết thiếu
M('ng2', '2324', 'I will lend you some money, but you must ______ it back to me next week.', 'pay|pays|to pay|paying', 'A', 'Sau <b>must</b> dùng động từ nguyên mẫu không "to": <b>pay</b>.')
M('ng2', '2324', 'Those audiences have to ______ their tickets before entering the concert hall.', 'showing|show|shows|To show', 'B', 'Sau <b>have to</b> dùng động từ nguyên mẫu: <b>show</b>.')
M('ng2', '2324', 'This drink isn\'t beneficial for health. You ______ drink it too much.', 'should|ought to|ought not to|mustn\'t', ['C', 'D'], 'Đồ uống không tốt → lời khuyên/cấm: <b>ought not to</b> hoặc <b>mustn\'t</b> (không nên/không được). should/ought to khẳng định sai nghĩa.')
M('ng2', '2324', 'I think you ______ do exercise regularly in order to keep your body in good shape.', 'must|should|ought not to|shouldn\'t', 'B', 'Lời khuyên "I think you …" → <b>should</b>. ought not to / shouldn\'t phủ định sai nghĩa; must quá mạnh.')
M('ng2', '2324', 'All students ______ wear uniforms at school because it is a rule.', 'should|have to|ought to|must', ['B', 'D'], 'Quy định bắt buộc ("it is a rule") → <b>have to</b> hoặc <b>must</b>.')
M('ng2', '2324', 'This warning sign indicates that you ______ step on the grass.', 'shouldn\'t|mustn\'t|don\'t have to|ought not to', 'B', 'Biển cảnh báo → điều bị cấm: <b>mustn\'t</b>. don\'t have to = không cần thiết (sai nghĩa).')
M('ng2', 'tn', 'According to the school regulations, you ______ go to school on time on the weekday.', 'should|must|have to|can', ['B', 'C'], 'Quy định của trường (bắt buộc) → <b>must</b> hoặc <b>have to</b>. should chỉ là lời khuyên; can = có thể.')
M('ng2', 'tn', 'Children ______ break the rules, or quarrel with parents.', 'must|mustn\'t|have to|don\'t have to', 'B', 'Điều cấm → <b>mustn\'t</b> (không được). don\'t have to = không cần.')
M('ng2', '2425', 'Students ______ look at their notes during the test.', 'don\'t have to|shouldn\'t|mustn\'t|ought not to', 'C', 'Quy chế thi cấm xem tài liệu → <b>mustn\'t</b> (cấm). don\'t have to = không cần thiết (sai nghĩa).')
N('ng2 (2425 Ex3 #15): shouldn\'t / ought not to cũng đúng ngữ pháp nhưng yếu hơn; khoá lấy mustn\'t (C) theo nghĩa "cấm trong khi thi".')
M('ng2', '2425', 'You ______ find time for some relaxation every day.', 'have to|must|should|might', 'C', 'Lời khuyên chung → <b>should</b> (nên). have to/must quá mạnh; might = có thể.')
M('ng2', '2425', 'All students ______ wear uniforms at school because it is a rule.', 'have to|should|must|mustn\'t', ['A', 'C'], 'Quy định bắt buộc → <b>have to</b> hoặc <b>must</b>.')
M('ng2', '2425', 'I suggest that GenZ ______ be encouraged to develop their digital skills and passion for social change.', 'mustn\'t|should|may|have', 'B', 'Cấu trúc <b>suggest (that) + S + (should) + V</b> → should be encouraged.')

# ---- ng3: động từ nối / trạng thái / dạng từ / bị động / tương lai
M('ng3', '2324', 'He ______. What\'s wrong with him?', 'looks so worried|looks so worriedly|is looking so worried|is looking so worriedly', 'A', '<b>look</b> là linking verb → theo sau là tính từ (worried). Dùng hiện tại đơn cho trạng thái/ấn tượng nên chọn <b>looks so worried</b>.')
M('ng3', '2324', 'This room ______ since I was born.', 'has been painted|was painted|painted|has painted', 'A', 'Câu bị động ("căn phòng được sơn") + <b>since</b> → hiện tại hoàn thành bị động: <b>has been painted</b>.')
M('ng3', '2324', 'The urban lifestyle seems more ______ to young people.', 'excite|excited|exciting|excitingly', 'C', '<b>seem</b> là linking verb + tính từ; chủ ngữ là sự vật (lifestyle) → tính từ V-ing: <b>exciting</b>.')
M('ng3', '2324', 'What\'s the matter? You look ______.', 'happily|happiness|unhappy|unhappily', 'C', '<b>look</b> + tính từ; nghĩa "có chuyện gì thế" → <b>unhappy</b>.')
M('ng3', '2324', 'That kitten\'s fur ______ so soft.', 'looks|sounds|smells|tastes', 'A', 'Lông mèo mềm là điều nhìn/cảm nhận được → <b>looks</b> (sounds/smells/tastes không hợp nghĩa).')
M('ng3', '2324', 'The waves crashed on the shore where they ______ cool on my hot feet.', 'appeared|felt|looked|sounded', 'B', 'Cảm giác lạnh trên chân → <b>felt</b> cool (linking verb + tính từ).')
M('ng3', '2324', 'The room smells ______ and needs cleaning ______.', 'bad/immediately|badly/immediate|badly/immediately|bad/immediate', 'A', '<b>smell</b> là linking verb → tính từ <b>bad</b>; "needs cleaning" bổ nghĩa bằng trạng từ <b>immediately</b>.')
M('ng3', '2324', 'Mr. Brown looked ______ when hearing his son talking to his friends so ______.', 'angry/impolite|angry/impolitely|angrily/impolite|angrily/impolitely', 'B', '<b>looked</b> + tính từ (angry); "talking … so ___" bổ nghĩa cho động từ talk → trạng từ <b>impolitely</b>.')
M('ng3', 'tn', 'Although the dish smelt ______, he refused to eat saying that he was not hungry.', 'bad|good|well|worse', 'B', '<b>smell</b> + tính từ. "Although" chỉ sự tương phản: món ăn thơm (<b>good</b>) nhưng anh vẫn từ chối vì không đói.')
N('ng3 (tn "Although the dish melt ___"): "melt" là lỗi gõ của "smelt" (smell, quá khứ); khoá chọn good (B).')
M('ng3', '2425', 'The fish tastes ______, I won\'t eat it.', 'awful|awfully|more awfully|as awful', 'A', '<b>taste</b> + tính từ: <b>awful</b> (kinh khủng).')
M('ng3', '2425', 'The situation looks ______. We must do something.', 'good|well|bad|badly', 'C', '<b>look</b> + tính từ; "We must do something" → tình hình xấu → <b>bad</b>.')
M('ng3', '2425', 'My best friend didn\'t show up for the English club. So I was ______.', 'disappointingly|disappointing|disappointed|disappointment', 'C', 'Chỉ cảm xúc của người → tính từ V-ed: <b>disappointed</b>.')
M('ng3', '2425', 'The cake tastes ______.', 'good|goodly|well|badly', 'A', '<b>taste</b> (linking verb) + tính từ → <b>good</b>.')
M('ng3', '2425', 'Listen! Her story ______ interesting.', 'sounds|is sounding|sound|was sounding', 'A', '<b>sound</b> là động từ trạng thái, không dùng tiếp diễn; chủ ngữ số ít → <b>sounds</b>.')
M('ng3', '2425', 'These dresses ______ for the cultural event by my aunt.', 'sewed|were sewed|have been sewed|have sewed', 'B', 'Bị động + "by my aunt" (hành động đã xảy ra): <b>were sewed</b> (chuẩn hơn là were sewn; đề không có phương án này).')
N('ng3 (minh hoạ #12): đúng chuẩn là "were sewn"; đề chỉ có "were sewed" nên chọn B.')
M('ng3', '2425', 'I think I ______ home tonight. I\'m a little tired.', 'stay|am staying|will stay|will be staying', 'C', 'Quyết định đưa ra ngay tại lúc nói ("I think I … I\'m a little tired") → <b>will stay</b>.')

# ---- ng4: chia động từ (fill)
F('ng4', '2425', 'She {_} so beautiful in that white dress.', ['looks', 'looked'], '<b>look</b> là linking verb, chia hiện tại đơn: <b>looks</b> (cũng chấp nhận looked nếu hiểu là câu kể quá khứ).', hint='look')
F('ng4', '2425', 'She wants to {_} a fashion designer like Victoria Beckham in the future.', ['become'], 'want to + V nguyên mẫu: <b>become</b>.', hint='become')
F('ng4', '2425', 'Teenagers like to make their own choice when they {_} older.', ['grow'], 'Mệnh đề thời gian với "when" chỉ chân lý chung → hiện tại đơn: they <b>grow</b> older.', hint='grow')
F('ng4', '2425', 'Turn on the fan. It {_} hotter and hotter.', ['is getting', "'s getting"], 'Diễn tả sự thay đổi đang diễn ra → hiện tại tiếp diễn: <b>is getting</b> hotter and hotter.', hint='get')
F('ng4', '2425', 'That Super Junior {_} suddenly at the end of concert makes its fans overjoyed.', ['appearing', 'appeared'], 'Chủ ngữ là mệnh đề danh hoá "That + S + V …" hoặc danh động từ; cách dùng thông thường: <b>appearing</b> (Super Junior xuất hiện bất ngờ làm fan vui sướng).', hint='appear')
F('ng4', '2425', 'David {_} about holding a party next weekend.', ['is thinking'], '<b>think about</b> (cân nhắc, đang nghĩ đến) là hành động → có thể dùng tiếp diễn: <b>is thinking</b>.', hint='think')
F('ng4', '2425', 'Why {_} you {_} the flowers?', {'blanks': [['are'], ['smelling']]}, '<b>smell</b> (ngửi bằng mũi – hành động chủ động) có thể dùng tiếp diễn: Why <b>are</b> you <b>smelling</b> the flowers?', hint='smell')
F('ng4', '2425', 'Last night I {_} my keys. I had to call my flatmate to let me in.', ['lost'], 'Mốc quá khứ xác định (<b>last night</b>) → quá khứ đơn: <b>lost</b>.', hint='lose')
F('ng4', '2425', 'My bicycle isn\'t here. I think someone {_} it.', ['has just taken', "has taken", "'s just taken"], 'Hành động vừa xảy ra, kết quả ở hiện tại (xe không còn) → hiện tại hoàn thành: <b>has just taken</b>.', hint='just/take')
F('ng4', '2425', 'How many {_} are there in the competition?', ['participants'], 'Sau "How many" cần danh từ số nhiều chỉ người: <b>participants</b> (người tham gia).', hint='participate')
F('ng4', '2425', 'He {_} me a big teddy bear on my birthday last week.', ['bought'], 'Mốc quá khứ xác định (<b>last week</b>) → quá khứ đơn: <b>bought</b>.', hint='buy')
F('ng4', '2425', 'Sorry about that! I {_} really busy since my birthday.', ['have been', "'ve been"], '<b>since + mốc</b> → hiện tại hoàn thành: <b>have been</b>.', hint='be')
F('ng4', '2425', 'They {_} each other since they were children.', ['have known'], '<b>since they were children</b> → hiện tại hoàn thành; "know" là động từ trạng thái nên dùng <b>have known</b> (không dùng tiếp diễn).', hint='know')
N('ng4 (2425 Writing I #5): "That Super Junior (appear) suddenly … makes its fans overjoyed" – dạng đúng là appearing (chủ ngữ danh động từ); chấp nhận thêm appeared.')
N('ng4 (2425 Writing I #6, #7): think about / smell là động từ có hai nghĩa: ở nghĩa "cân nhắc / ngửi" dùng được tiếp diễn → is thinking; are … smelling.')

# ======================================================================================
# TÌM LỖI SAI
# ======================================================================================
E('er1', '2223', 'We <u>ought to not</u> play football <u>as</u> <u>it\'s raining</u> <u>outside</u>.', 'A', 'Phủ định của <b>ought to</b> là <b>ought not to</b>. Sửa: ought to not → ought not to.')
E('er1', '2223', 'We <u>needn\'t</u> drive <u>fast</u>; <u>there is</u> a <u>speed limit</u> here.', 'A', 'Có giới hạn tốc độ → điều bị cấm nên phải dùng <b>mustn\'t</b> (không được), không phải needn\'t (không cần). Sửa: needn\'t → mustn\'t.')
E('er1', '2223', 'I <u>stayed</u> up <u>late</u> last night because I <u>mustn\'t</u> go to school <u>on</u> Sunday.', 'C', 'Chủ nhật không phải đến trường → "không cần" = <b>didn\'t have to</b> (quá khứ). Sửa: mustn\'t → didn\'t have to.')
E('er1', '2223', 'You <u>don\'t have to</u> <u>take</u> photographs <u>here</u>. This is a <u>restricted</u> area.', 'A', 'Khu vực hạn chế → bị cấm chụp ảnh → <b>mustn\'t</b>. Sửa: don\'t have to → mustn\'t.')
E('er1', '2223', 'Nicole grew <u>tired</u> from the <u>hours</u> of overtime at work. It <u>became</u> quite <u>obviously</u> that she needed a long vacation.', 'D', 'Sau <b>became quite</b> cần tính từ: <b>obvious</b>, không phải trạng từ obviously.')
E('er1', '2223', 'I <u>feel</u> both <u>excited</u> and <u>nervously</u> because I have got a date <u>with</u> Daisy tomorrow.', 'C', '<b>feel</b> là linking verb → dùng tính từ song song với "excited": <b>nervous</b>. Sửa: nervously → nervous.')
E('er1', '2223', '<u>All</u> the <u>members of</u> the committee <u>felt happily</u> about the <u>ultimate decision</u>.', 'C', '<b>felt</b> + tính từ: felt <b>happy</b>. Sửa: felt happily → felt happy.')
E('er1', '2223', 'After <u>being closed</u> for <u>a long period of</u> time, the house <u>became dirty</u> and <u>smelled awfully</u>.', 'D', '<b>smell</b> là linking verb → tính từ: smelled <b>awful</b>. Sửa: smelled awfully → smelled awful.')
E('er1', '2324', 'I <u>wash</u> the dishes <u>yesterday</u>, but I <u>have not</u> had the time yet to do it <u>today</u>.', 'A', 'Có <b>yesterday</b> → quá khứ đơn: wash → <b>washed</b>.')
E('er1', '2324', 'The children <u>have put</u> away their toys <u>but</u> they <u>didn\'t make</u> their beds <u>yet</u>.', 'C', 'Có <b>yet</b> → hiện tại hoàn thành: didn\'t make → <b>haven\'t made</b>.')
E('er1', '2324', 'She spoke <u>in a very</u> low voice, <u>but</u> I <u>can</u> understand what <u>she said</u> a few minutes ago.', 'C', 'Hành động trong quá khứ ("a few minutes ago") → can → <b>could</b> (hoặc "was able to").')
E('er1', '2324', 'I <u>haven\'t played</u> football <u>when</u> I was at school but I <u>was</u> very good <u>at</u> it then.', 'A', 'Có mốc quá khứ <b>when I was at school</b> → quá khứ đơn: haven\'t played → <b>didn\'t play</b>.')
E('er1', '2324', '<u>Without</u> the <u>particularly</u> habitat, the species <u>could</u> not <u>survive</u> any more.', 'B', 'Trước danh từ "habitat" cần tính từ: particularly → <b>particular</b>.')
E('er1', '2324', 'My <u>personal trainer</u> suggested that I <u>must do</u> some <u>warm-up activities</u> before starting the <u>main tasks</u>.', 'B', 'Sau <b>suggest (that)</b> dùng (should) + V nguyên mẫu: must do → <b>should do</b>.')
E('er1', '2324', 'We <u>ought to not</u> play football <u>as</u> <u>it\'s raining</u> <u>outside</u>.', 'A', 'Phủ định đúng là <b>ought not to</b>.')
E('er1', '2324', 'You <u>have to</u> <u>made</u> sure that children <u>don\'t</u> play outside <u>alone</u>.', 'B', 'Sau <b>have to</b> dùng động từ nguyên mẫu: made → <b>make</b>.')
E('er1', '2324', 'You <u>mustn\'t</u> <u>uses</u> the motorbike <u>without</u> a driver\'s license. It\'s <u>against</u> the law.', 'B', 'Sau <b>mustn\'t</b> dùng động từ nguyên mẫu: uses → <b>use</b>.')
E('er1', '2324', 'Drivers <u>haven\'t</u> <u>to stop</u> at <u>yellow</u> traffic <u>lights</u>.', 'A', '"Không cần" là <b>don\'t have to</b> (không có "haven\'t to"). Sửa: haven\'t to stop → don\'t have to stop.')
E('er1', '2324', '<u>According to</u> the rules <u>of</u> this game, you <u>had better not</u> <u>drop</u> the ball.', 'C', 'Theo luật chơi (<b>according to the rules</b>) là điều bị cấm → dùng <b>mustn\'t</b>; "had better not" chỉ là lời khuyên.')
N('er1 (2324 U2 #5 "had better not"): câu gốc khó xác định lỗi (nhãn A–D lệch); chọn C (had better not → mustn\'t) – hơi mơ hồ.')
E('er1', '2324', '<u>The</u> school regulations <u>say</u> that students <u>don\'t have to</u> <u>fight</u> each other.', 'C', 'Đánh nhau là điều bị cấm → <b>mustn\'t</b>, không phải don\'t have to (không cần).')
N('er1 (2324 U2 #6): nguồn gạch chân 5 đoạn nhưng chỉ có nhãn A–D; đã gộp "don\'t have to" thành một mục C.')
N('er1 (2324 U1 #34): nguồn không gạch chân "haven\'t played"; đã chuyển gạch chân sang cụm này (đáp án A).')
E('er1', '2324', 'I <u>am thinking</u> that <u>living</u> in the city <u>is</u> good <u>for</u> young people.', 'A', '<b>think</b> với nghĩa "cho rằng" là động từ trạng thái, không dùng tiếp diễn: am thinking → <b>think</b>.')
E('er1', '2324', 'I <u>am not seeing</u> <u>the</u> building. <u>It\'s</u> too far <u>away</u>.', 'A', '<b>see</b> (nhìn thấy) không dùng tiếp diễn: am not seeing → <b>don\'t see</b> (hoặc can\'t see).')
E('er1', '2324', '<u>My</u> girlfriend <u>looks</u> <u>adorably</u> when <u>wearing</u> this skirt.', 'C', '<b>look</b> là linking verb → tính từ: adorably → <b>adorable</b>.')
E('er1', '2324', 'The milk <u>smells</u> <u>terribly</u>, <u>so</u> you should throw it <u>away</u>.', 'B', '<b>smell</b> là linking verb → tính từ: terribly → <b>terrible</b>.')
E('er1', '2324', 'The waste <u>disposed</u> system <u>is</u> also innovative. There are no rubbish trucks <u>or</u> waste bins <u>in</u> the street.', 'A', 'Cần danh từ ghép "waste disposal system" (hệ thống xử lý rác): disposed → <b>disposal</b>.')
E('er1', '2324', 'Vancouver <u>is</u> often considered <u>to be</u> one of the most <u>living</u> cities <u>in</u> the world.', 'C', '"one of the most … cities" cần tính từ <b>livable</b> (đáng sống), không phải "living".')
E('er1', 'tn', 'After <u>being closed</u> for <u>a long period of</u> time, the house <u>became dirty</u> and <u>smelled awfully</u>.', 'D', 'smell + tính từ: smelled <b>awful</b>.')
E('er1', 'tn', '<u>All</u> the <u>members of</u> committee <u>felt happily</u> about the <u>ultimate decision</u>.', 'C', 'felt + tính từ: felt <b>happy</b>.')
E('er1', 'tn', 'I <u>feel</u> both <u>excited</u> and <u>nervously</u> because I have got a <u>date with</u> Lara tomorrow.', 'C', 'feel + tính từ: nervously → <b>nervous</b>.')
E('er1', 'tn', 'He <u>looks</u> so <u>worriedly</u>. What\'s <u>wrong</u> <u>with</u> him?', 'B', 'look là linking verb + tính từ: worriedly → <b>worried</b>.')
E('er1', 'tn', 'I <u>think</u> about <u>buying</u> <u>a</u> flat <u>in</u> Ha Noi.', 'A', '"Đang cân nhắc mua căn hộ" là hành động → dùng tiếp diễn: think → <b>am thinking</b> (think about = suy nghĩ về).')
E('er1', 'tn', 'My uncle <u>is having</u> <u>a</u> big house <u>in</u> the city <u>centre</u>.', 'A', '<b>have</b> (sở hữu) là động từ trạng thái, không dùng tiếp diễn: is having → <b>has</b>.')
E('er1', 'tn', '<u>Are you remembering</u> when the <u>sensors</u> were <u>installed</u> in <u>the</u> city?', 'A', '<b>remember</b> là động từ trạng thái: Are you remembering → <b>Do you remember</b>.')
E('er1', 'tn', 'I <u>am seeing</u> your point, <u>but</u> I <u>don\'t think</u> there\'s <u>anything</u> we can do at the moment.', 'A', '<b>see</b> (hiểu) là động từ trạng thái: am seeing → <b>see</b>.')

# ======================================================================================
# ĐIỀN TỪ / ĐỌC ĐIỀN / SẮP XẾP CÂU
# ======================================================================================
def blank(g, s, n, opts, ans, exp):
    M(g, s, 'Chỗ trống (%d)' % n, opts, ans, exp)


# dt1 – families
blank('dt1', '2223', 1, 'Although|However|Unless|Besides', 'A', '<b>Although</b> + mệnh đề: "Mặc dù số giờ mẹ ở nhà giảm … nhưng sự quan tâm cho mỗi đứa tăng". However đứng đầu câu với dấu phẩy; unless = nếu không.')
blank('dt1', '2223', 2, 'isolated|individual|unique|single', 'B', '<b>individual attention</b> = sự quan tâm riêng cho từng đứa trẻ.')
blank('dt1', '2223', 3, 'adding|counting|taking|including', 'D', '<b>including those who work</b> = bao gồm cả những người đi làm.')
blank('dt1', '2223', 4, 'whom|which|who|when', 'C', 'Đại từ quan hệ thay cho "people" (chủ ngữ): <b>who raised children</b>.')
blank('dt1', '2223', 5, 'helping|to help|help|on help', 'A', '<b>spend time + V-ing</b>: spend more time <b>helping</b> with homework.')
# dt2 – Dutch
blank('dt2', '2223', 1, 'golden|iron|solid|fixed', 'A', '<b>golden rule</b> = quy tắc vàng.')
blank('dt2', '2223', 2, 'compared|put|rated|assessed', 'C', '<b>be rated (as) Europe\'s most fortunate</b> = được xếp hạng/đánh giá là may mắn nhất châu Âu.')
blank('dt2', '2223', 3, 'regarded|valued|recognized|measured', 'B', '<b>opinions are valued</b> (ý kiến được trân trọng), song song với "wishes respected".')
blank('dt2', '2223', 4, 'argue|criticize|defend|judge', 'A', '<b>Some would argue that …</b> = Một số người sẽ cho rằng.')
blank('dt2', '2223', 5, 'resulted|created|brought|turned', 'D', '<b>turn … into</b> = biến … thành (turned a whole generation into spoilt brats).')
# dt3 – Dad
blank('dt3', '2223', 1, 'men|someone|person|anyone', 'C', 'He is the <b>person</b> who provides … (người cung cấp tiền cho gia đình).')
blank('dt3', '2223', 2, 'bringing|taking|to take|to bring', 'B', '<b>be useful for + V-ing</b>; <b>take you in the car to</b> parties = chở bạn đến (bring dùng cho hướng về người nói).')
blank('dt3', '2223', 3, 'explains|shouts|complains|groans', 'C', '<b>complain about</b> = phàn nàn về thời gian nói chuyện điện thoại.')
blank('dt3', '2223', 4, 'support|give|bring|call', 'A', '<b>support you in an argument</b> = ủng hộ bạn trong cuộc tranh cãi.')
blank('dt3', '2223', 5, 'report|result|revise|review', 'A', '<b>school report</b> = phiếu báo/nhận xét học tập.')
# dt4 – healthy relationship
blank('dt4', '2223', 1, 'another\'s|each onother\'s|each other\'s|one another', 'C', '<b>each other\'s differences</b> = những điểm khác biệt của nhau (sở hữu cách).')
blank('dt4', '2223', 2, 'effective|effectively|effectiveness|ineffective', 'B', 'Bổ nghĩa cho động từ "communicate": trạng từ <b>effectively</b>.')
blank('dt4', '2223', 3, 'violent|non-violent|violently|violence', 'B', 'Song song với "rational and …" (tính từ) và hợp nghĩa giải quyết xung đột: <b>non-violent way</b>.')
blank('dt4', '2223', 4, 'asks|calls|looks|requires', 'D', 'Chủ ngữ là hành động duy trì mối quan hệ: <b>requires skills</b> = đòi hỏi kỹ năng.')
blank('dt4', '2223', 5, 'bringing|growing|raising|taking', 'B', '<b>growing up</b> = lớn lên (song song với "a lack of these skills, and growing up in a society …").')
# dt5 – exercise & character
blank('dt5', 'tn', 1, 'down|out|in|up', 'D', '<b>take up</b> a sport = bắt đầu chơi/theo một môn thể thao.')
blank('dt5', 'tn', 2, 'who|whose|which|what', 'A', 'Thay cho "those" (người) làm chủ ngữ: <b>those who</b> like to be with other people.')
blank('dt5', 'tn', 3, 'therefore|thus|however|while', 'C', 'Vế sau đối lập với vế trước (thích đi cùng người khác ↔ thích ở một mình) → <b>However,</b>.')
blank('dt5', 'tn', 4, 'winners|winning|win|won', 'B', 'Chủ ngữ của "isn\'t important" → danh động từ <b>winning</b> (việc chiến thắng).')
blank('dt5', 'tn', 5, 'challenge|victory|defeat|score', 'A', '<b>an enjoyable challenge</b> = một thử thách thú vị, không cần hơn ai.')
blank('dt5', '2425', 1, 'down|out|in|up', 'D', '<b>take up</b> a sport.')
blank('dt5', '2425', 2, 'who|whose|which|what', 'A', '<b>those who</b> like …')
blank('dt5', '2425', 3, 'therefore|thus|however|while', 'C', '<b>However,</b> (đối lập).')
blank('dt5', '2425', 4, 'winners|winning|win|won', 'B', '<b>winning</b> (danh động từ làm chủ ngữ).')
# dt6 – driverless cars
blank('dt6', 'tn', 1, 'look|sound|feel|sense', 'B', '<b>sound like</b> = nghe có vẻ như (something from the future).')
blank('dt6', 'tn', 2, 'if|where|why|what', 'A', '<b>warn the driver if</b> they are slipping out of the right lane = cảnh báo tài xế nếu xe trượt khỏi làn.')
blank('dt6', 'tn', 3, 'nicely|quickly|harmlessly|safely', 'D', 'Vượt xe khác một cách <b>safely</b> (an toàn) – hợp với ưu điểm xe tự lái.')
blank('dt6', 'tn', 4, 'too closer|much closer|very closely|so closest', 'B', 'So sánh hơn: <b>much closer to each other</b> (nhấn mạnh bằng "much").')
blank('dt6', 'tn', 5, 'inaccuracy|offence|error|crime', 'C', '<b>human error</b> = lỗi do con người.')
# dt7 – healthy life
blank('dt7', 'tn', 1, 'well|good|badly|bad', ['A', 'B'], '<b>feel well / feel good</b> đều đúng (sau linking verb "feel" dùng tính từ; well = khoẻ mạnh).')
blank('dt7', 'tn', 2, 'doing|making|playing|having', 'C', '<b>play sports</b> = chơi thể thao.')
blank('dt7', 'tn', 3, 'charge|care|note|advantage', 'B', '<b>take care of</b> = chăm sóc.')
blank('dt7', 'tn', 4, 'where|who|when|that', 'D', 'Đại từ quan hệ thay cho "things" (vật): <b>things that can harm us</b>.')
blank('dt7', 'tn', 5, 'be|are|getting|Ø', 'C', 'Song song với "have more fun, … happier": <b>getting</b> happier (ngày càng hạnh phúc hơn).')
N('dt7 (tn cloze 6 #1): feel well (A) và feel good (B) đều đúng → chấp nhận A, B.')
# dt8 – meditation ad
blank('dt8', '2425', 1, 'negative|rare|regular|anual', 'C', '<b>regular practice</b> = việc luyện tập đều đặn, phù hợp thói quen hằng ngày.')
blank('dt8', '2425', 2, 'busy|hard-working|frustrated|balanced', 'D', '<b>a balanced and peaceful life</b> = cuộc sống cân bằng và bình yên.')
blank('dt8', '2425', 3, 'reserve|cancel|secure|postpone', ['A', 'C'], '<b>reserve / secure your spot</b> = giữ chỗ. cancel = huỷ; postpone = hoãn.')
N('dt8 (2425 Ex4 #12): reserve (A) và secure (C) đều đúng nghĩa "giữ chỗ" → chấp nhận A, C.')
# dt9 – vaccination
blank('dt9', '2425', 1, 'announce|control|suggest|focus', 'A', '<b>We are pleased to announce that …</b> = chúng tôi vui mừng thông báo rằng.')
blank('dt9', '2425', 2, 'in|on|of|with', 'B', 'Giới từ chỉ ngày: <b>on March 15th</b>.')
blank('dt9', '2425', 3, 'advise|advice|advisable|advisedly', 'C', 'Sau "It is also" cần tính từ: <b>advisable</b> (nên làm).')
# dt10 – situation wanted
blank('dt10', '2425', 1, 'the|no article|a|an', 'B', '<b>with experience of 7 years</b> – "experience" không đếm được, không cần mạo từ.')
blank('dt10', '2425', 2, 'leading|leaded|leader|led', 'A', '<b>leading International schools</b> = các trường quốc tế hàng đầu (tính từ).')
blank('dt10', '2425', 3, 'in|on|with|at', 'A', '<b>fluent in English</b>.')
# dt11 – airline
blank('dt11', '2425', 1, 'take|make|have|wait', 'A', '<b>Take a minute to</b> locate … = dành chút thời gian để tìm …')
blank('dt11', '2425', 2, 'should|if|unless|when', 'A', 'Đảo ngữ điều kiện loại 1: <b>Should the cabin experience</b> sudden pressure loss (= If the cabin should experience …). Động từ "experience" ở dạng nguyên mẫu nên không dùng "if".')
blank('dt11', '2425', 3, 'take off|descend|land|fly', 'A', '<b>While we wait for take-off</b> = trong lúc chờ máy bay cất cánh.')
# dt12 – generation gap Vietnam
blank('dt12', '2425', 1, 'both|either|neither|nor', 'A', '<b>both … challenges and opportunities</b>.')
blank('dt12', '2425', 2, 'comparing|compared|comparison|compare', 'B', '<b>compared to</b> = so với (rút gọn bị động).')
blank('dt12', '2425', 3, 'Since|However|Therefore|Moreover', 'B', 'Vế sau đối lập với vế trước (khoảng cách → cơ hội học hỏi) → <b>However,</b>.')
blank('dt12', '2425', 4, 'On|In|From|By', 'D', '<b>By + V-ing</b> = bằng cách (by fostering open dialogue …).')
blank('dt12', '2425', 5, 'bring|earn|harness|utilize', ['C', 'D'], '<b>harness / utilize the positive aspects</b> = tận dụng những mặt tích cực. bring/earn không đi với cụm này.')
N('dt12 (2425 #28): harness (C) và utilize (D) đều hợp nghĩa → chấp nhận C, D.')

# dt13 – sắp xếp câu
M('dt13', '2425', 'a. In addition, avoiding smoking and limiting alcohol consumption are crucial for lung and liver health.<br>b. Overall, adopting these habits can lead to a significantly improved quality of life.<br>c. Drinking plenty of water is also vital for maintaining proper hydration and bodily functions.<br>d. Furthermore, regular medical check-ups can catch potential health issues early on.<br>e. Living a healthy lifestyle involves multiple factors that contribute to physical and mental well-being.',
  'e - c - a - d - b|c - e - a - d - b|e - d - c - a - b|a - e - c - d - b', 'A', 'e (câu mở đầu giới thiệu chủ đề) → c (also: uống nhiều nước) → a (in addition: tránh thuốc lá, rượu) → d (furthermore: khám sức khoẻ) → b (Overall: kết luận). Đáp án <b>e - c - a - d - b</b>.')
M('dt13', '2425', 'a. I intend to invite about 10 people, so it will be a small gathering.<br>b. Dear Jane, As the school year is coming to an end, I\'m giving a farewell party before we go away for holiday.<br>c. I will order some pizzas and buy snacks and fruits. There will be dancing and karaoke competition, so there will be a lot of fun.<br>d. Would you like to come?<br>e. It will be held at my home at 7 p.m this coming Sunday.<br>f. Please let me know if you can come. Just leave me a message on the phone if you can\'t catch me at home. Your friend,',
  'b - d - e - a - c - f|b - c - a - e - d - f|b - e - d - a - c - f|b - a - d - e - c - f', 'B', 'b mở đầu thư (có "Dear Jane"); c giới thiệu bữa tiệc sẽ có gì → a quy mô khách mời → e thời gian, địa điểm → d lời mời "Would you like to come?" → f đề nghị báo lại và kết thư. Đáp án <b>b - c - a - e - d - f</b>.')
N('dt13 (2425 minh hoạ Q22): thứ tự hợp lý nhất theo đề là b-c-a-e-d-f (B); phương án C (b-e-d-a-c-f) cũng đọc được nhưng lời mời xuất hiện quá sớm → giữ B, hơi mơ hồ.')
M('dt13', '2425', 'a. Also, voluntary tasks help them connect with the community, making them aware of the needs around them.<br>b. In addition to this, students develop teamwork and communication skills while they volunteer.<br>c. Firstly, they will gain valuable real-world experience which can help in their future careers.<br>d. Last but not least, doing volunteer work can be a rewarding job, as students feel great about helping others.<br>e. Upper secondary school students get many benefits from doing voluntary work.',
  'e - a - c - b - d|c - e - a - b - d|c - a - b - d - e|e - c - a - b - d', 'D', 'e (câu chủ đề) → c (Firstly) → a (Also) → b (In addition to this) → d (Last but not least). Đáp án <b>e - c - a - b - d</b>.')

# ======================================================================================
# ĐỌC HIỂU
# ======================================================================================
# dh1 – alternative schools
M('dh1', '2223', 'Which of the following is NOT true about 24-hour teaching?', 'Students can come to school from 7 a.m. to 10 p.m.|Students can study online at night.|Students can choose the time to study.|Some students need to study in the morning and some need to study at night.', 'D', 'Bài chỉ nói "some students <i>learn better</i> at night / in the morning" (học tốt hơn), không phải "need to study" (bắt buộc). A, B, C đều đúng với đoạn 1. Chọn <b>D</b>.')
M('dh1', '2223', 'According to Cheryl Heron, teaching ______.', 'should happen throughout the night|is not necessarily carried out in class|is for children who will not come to school|must be around the year', 'B', '"Why must teaching only be conducted in a classroom? You can teach a child without him ever coming to school." → dạy học <b>không nhất thiết phải diễn ra trong lớp</b>.')
M('dh1', '2223', 'Steiner schools don\'t ______.', 'encourage children\'s creativity and free thinking|allow teachers to teach things out of textbooks|teach reading and writing to young children|teach music to children', 'C', '"They don\'t have to learn to read and write at an early age." → không dạy đọc, viết cho trẻ nhỏ. (A, D trái bài; B sai: ở một số trường giáo viên không được dùng sách.)')
M('dh1', '2223', 'The word "this" in paragraph 3 refers to ______.', 'starting as young as possible|the violin|playing difficult pieces of music|learning their mother tongue', 'C', '"Even two-year-old children can learn to play difficult pieces of classical music … They do <u>this</u> by watching and listening" → <b>playing difficult pieces of music</b>.')
M('dh1', '2223', 'The word "involved" in paragraph 3 is closest in meaning to ______.', 'engaged|encouraging|accepting|rejecting', 'A', '<b>involved</b> = có tham gia ≈ <b>engaged</b> (tham gia, gắn bó).')
# dh2 – relationships
M('dh2', '2223', 'Teenagers go to their friends in order to ______.', 'impact them in various ways and the same amount.|ask how to dress when being around certain people.|have different relationships that their parents can\'t offer.|ask for help or advice that their parents can\'t give them.', 'D', '"Teenagers go to their friends for help or to ask questions that they could not ask their parents about." → <b>D</b>.')
M('dh2', '2223', 'Love relationships may make a teenager harder to get a good education because ______.', 'their boyfriend or girlfriend may make them fail in school|they tell their boyfriend or girlfriend how to dress to how to act|they hang out with their boyfriend or girlfriend instead of studying|they try to do their work instead of hanging out with their boyfriend or girlfriend.', 'C', '"Some start to fail in school because they are hanging out with their boyfriend or girlfriend instead of doing their work." → <b>C</b>.')
M('dh2', '2223', 'All of the following statements about parents\' influence on teenagers are true EXCEPT that ______.', 'achievements of teenagers from a family break-up are always slow.|parents have a great impact on teenagers.|most teenagers grow up to act and do things just like their parents.|a family break-up may have a negative effect on teenagers.', 'A', 'Bài chỉ nói trẻ có gia đình tan vỡ "<i>may</i> have lower achievements"; "<b>always</b> slow" là tuyệt đối hoá → sai. Chọn A.')
M('dh2', '2223', 'Relationships can ______.', 'influence teenagers in many aspects of their lives.|help teenagers to decide the future goals in love relationships.|help others to form relationships.|help teenagers to follow their future goals with their friends and family.', 'A', 'Cả bài nói các mối quan hệ ảnh hưởng đến nhiều khía cạnh trong cuộc sống thiếu niên → <b>A</b>.')
M('dh2', '2223', 'The main idea of the passage is ______.', 'the effects of love relationships on teenagers\' study.|the impact of relationships on teenagers\' lives.|the role of parents in their children\'s lives.|the impact of relationships on adults and teenagers.', 'B', 'Bài bàn về tác động của các mối quan hệ (bạn bè, cha mẹ, tình yêu) lên cuộc sống thiếu niên → <b>B</b>.')
# dh3 – online dating
M('dh3', '2223', 'Which of the following statements is TRUE?', 'Most people who took part in the survey said it is not difficult to meet people online than elsewhere.|Jess Ross doesn\'t believe that online dating is changing the way people meet each other.|Research has shown that online dating is not a good way of meeting people.|Women are more likely to find their ideal partner online than men.', 'A', '62% đồng ý rằng gặp người trên mạng dễ hơn các cách khác → A đúng. B, C trái bài; D sai (nam giới có khả năng tìm thấy tình yêu nhiều hơn).')
M('dh3', '2223', 'The word "imperative" in paragraph 3 is closest in meaning to ______.', 'crucial|minor|optional|useless', 'A', '<b>imperative</b> = cấp thiết, bắt buộc ≈ <b>crucial</b>.')
M('dh3', '2223', 'According to Dr. Jeff Gavin, ______.', 'people need to study love systematically to date.|it is not essential to understand the factors in relationships formed via online dating sites.|online dating is becoming more and more popular.|nothing can influence satisfaction in relationships formed through the Internet.', 'C', '"But with the popularity of online dating, it is imperative we understand the factors …" → Dr. Gavin nói hẹn hò trực tuyến ngày càng phổ biến → <b>C</b>.')
M('dh3', '2223', 'Which of the following would serve as the best title for the passage?', 'Internet does in fact encourage old-fashioned courtship.|Online dating - a good way of meeting people.|Online dating is showed to help you find your perfect partner.|The revolution of online dating is alarming.', 'B', 'Nội dung chính: nghiên cứu cho thấy hẹn hò trực tuyến là cách gặp gỡ tốt → <b>B</b>.')
M('dh3', '2223', 'The passage is about ______.', 'one-to-one dating|speed dating|group dating|online dating', 'D', 'Cả bài nói về hẹn hò trực tuyến (<b>online dating</b>).')
# dh4 – college life
M('dh4', '2223', 'According to the writer, if students want to have medical treatment, they should ______.', 'be away|be familiar with medical needs|make arrangements|meet their parents', 'C', '"If ongoing medical … treatment is needed, arrangements should be made in advance" → <b>make arrangements</b>.')
M('dh4', '2223', 'The word "ongoing" is closest in meaning to ______.', 'continuing|short-term|brief|little', 'A', '<b>ongoing</b> = đang tiếp diễn ≈ <b>continuing</b>.')
M('dh4', '2223', 'College students should be aware that ______.', 'everything in college will be different|parents and teachers are not in college|structures must be provided by parents|structures must be provided by teachers', 'A', 'Bài nhấn mạnh kỹ năng, cấu trúc (môi trường, học tập, xã hội) ở đại học khác trung học → <b>A</b> là ý sát nhất; C, D trái bài.')
N('dh4 (2223 reading 4 #3): đáp án A là phương án sát nhất, nhưng cách diễn đạt khá rộng – khoá tự suy luận.')
M('dh4', '2223', 'Which of the following is NOT true about college life?', 'It is essential to have good communication skills.|Students must be responsible for their own decisions.|Students should know some living skills.|Students should not ask for help.', 'D', 'Bài khuyên sinh viên "be comfortable asking for help when needed" → D ("should not ask for help") sai.')
M('dh4', '2223', 'The word "overwhelming" is closest in meaning to ______.', 'simple|confusing|manageable|easy', 'B', '<b>overwhelming</b> = quá sức, choáng ngợp ≈ <b>confusing</b> (gây rối); các từ còn lại là nghĩa trái ngược.')
# dh5 – generation gap in America
M('dh5', 'tn', 'What is the passage mainly about?', 'The development of the generation gap in America nowadays.|The alleviation of the generation gap in America nowadays.|The eradication of the generation gap in America in the past.|The reduction of the generation gap in America in the past.', 'B', 'Bài nói căng thẳng giữa các thế hệ ở Mỹ <b>đã được giảm bớt</b> (alleviated) ngày nay → B.')
M('dh5', 'tn', 'What does the word "they" in line 6 mean?', 'Teenagers.|Forms of social media.|Parents.|Older generations', 'A', '"… they were exposed to various forms of social media … <u>They</u> got access to huge sources of new ideas" → <b>teenagers</b>.')
M('dh5', 'tn', 'According to the passage, what types of social media provided young people with new ideas in the 1960s?', 'The Internet and television.|The Internet and radios.|The television and printed newspaper.|The television and radios.', 'D', '"… exposed to various forms of social media like television and radios" → <b>D</b>.')
M('dh5', 'tn', 'Why did the older generation refuse to access new things?', 'Because they thought those things were tedious.|Because they loved to go to church every weekend.|Because they didn\'t want to change their normal life.|Because they weren\'t able to learn technological devices.', 'C', '"many older people were conservative and didn\'t accept differences disturbing their normal life" → <b>C</b>.')
M('dh5', 'tn', 'What can be inferred from the passage?', 'Nowadays there is no longer a generation gap.|The generation gap didn\'t remain after the 1960s.|Teaching older people to use modern devices can bridge the gap between generations.|Younger Americans are forced to change their taste in music nowadays.', 'C', 'Người già học dùng laptop/smartphone từ con cháu giúp giảm căng thẳng → có thể suy ra <b>C</b>. A, B tuyệt đối hoá; D không có trong bài.')
# dh6 – parent-teen
M('dh6', 'tn', 'What is the main idea of the passage?', 'Puberty of teenagers|Teens\' romantic relationship|Parent-teen relationship|Teens\' responsibilities', 'C', 'Bài bàn về mối quan hệ cha mẹ – thiếu niên và cách duy trì tốt → <b>C</b>.')
M('dh6', 'tn', 'According to the passage, who are pointed out to considerably influence young child?', 'their peers|their teachers|their parents|famous people', 'C', '"Parents have a huge influence on a young child\'s values and interests" → <b>their parents</b>.')
M('dh6', 'tn', 'The word "this" in paragraph 2 refers to ______.', 'Puberty brings lots of emotions for teens|Parents have a huge influence on a young child\'s values and interests|Both parents and teens need time to adapt the relationship|Parents cannot separate from their teens who want to be free', 'D', 'Câu trước: cha mẹ khó tách rời khỏi con trong khi con muốn tự do → "<u>This</u> may lead to conflict" chỉ <b>D</b>.')
M('dh6', 'tn', 'The word "willing" is CLOSEST in meaning to ______.', 'shocked|ready|strict|sympathetic', 'B', '<b>willing</b> = sẵn lòng ≈ <b>ready</b>.')
M('dh6', 'tn', 'Which of the following is NOT TRUE about the solution as teens get older?', 'Complain and resist|Communicate constantly|Set rules about routine and home life|Ask teens to take on responsibilities', 'A', 'Giải pháp gồm: giao trách nhiệm, đặt quy tắc rõ ràng, giao tiếp thường xuyên. "Complain and resist" là phản ứng của thiếu niên, không phải giải pháp → <b>A</b>.')
# dh7 – best time to exercise
M('dh7', 'tn', 'What is the text mainly about?', 'Workouts at different times and their benefits.|Drawbacks of afternoon workouts.|Advantages of evening workouts.|Benefits of morning workouts and injuries.', 'A', 'Bài so sánh lợi ích của tập luyện buổi sáng, chiều, tối → <b>A</b>.')
M('dh7', 'tn', 'Which of the following is a benefit of a morning workout?', 'You put on weight.|You gain more body fat.|You have a better night\'s sleep.|You have an empty stomach.', 'C', '"Morning exercise also helps many people sleep better at night." → <b>C</b>.')
M('dh7', 'tn', 'The word "endurance" in paragraph 2 means ______.', 'the ability to see problems and solve them quickly without others\' support|the ability to continue doing something painful or difficult for a long period of time|the ability to work both on your own and in a group|the ability to live a balanced life', 'B', '<b>endurance</b> = sức bền, khả năng chịu đựng làm việc khó nhọc trong thời gian dài → <b>B</b>.')
M('dh7', 'tn', 'Which of the following is a benefit of an afternoon or evening workout?', 'Your body temperature is the lowest.|Your reaction time is slow.|Your heart rate and blood pressure are the highest.|You can avoid the risk of injury.', 'D', '"Exercising at this time decreases your chances of injury" → <b>D</b>.')
M('dh7', 'tn', 'The word "its" in paragraph 2 refers to ______.', 'afternoon|reaction time|evening|heart rate', 'B', '"your reaction time is at <u>its</u> quickest" → <b>reaction time</b>.')
# dh8 – Super Size Me
M('dh8', '2425', 'Which of the following is the best title for the passage?', 'An experiment with McDonald\'s fast food|Putting on weight due to eating fast food|Connection between fast food and heart diseases|How fast food trigger liver damage', 'A', 'Cả bài kể về thí nghiệm ăn toàn đồ ăn nhanh McDonald\'s của Spurlock → <b>A</b>.')
M('dh8', '2425', 'Which of the following is TRUE about Morgan Spurlock?', 'He had to eat Super Size meal once a week.|He had to eat Super Size meal twice a day.|He had to eat Super Size meal three times a week.|He had to consume Super Size for three meals a day.', 'D', 'Ông ăn McDonald\'s ba bữa mỗi ngày, phải chọn Super Size khi được mời → <b>D</b>.')
M('dh8', '2425', 'In paragraph 2, the word "giant" is closest in meaning to ______.', 'light|balanced|big|healthy', 'C', '<b>giant</b> = khổng lồ ≈ <b>big</b>.')
M('dh8', '2425', 'Which of the following could get rid of Spurlock\'s headaches?', 'salad|a McDonald\'s meal|a pain killer|nothing', 'B', '"The only thing that got rid of his headaches … was another McDonald\'s meal" → <b>B</b>.')
M('dh8', '2425', 'According to the passage, all of the following are the results of the experiment EXCEPT ______.', 'Spurlock put on weight|the experiment affected his heart|the experiment affected his liver|he became fairly relaxed and energetic', 'D', 'Ông bị trầm cảm, mất năng lượng, tim và gan có vấn đề → "relaxed and energetic" không phải kết quả → <b>D</b>.')
M('dh8', '2425', 'The word "its" in paragraph 4 refers to ______.', 'McDonald\'s|the experiment|the film Super Size Me|the menu', 'C', '"Just after <u>its</u> showing in 2004 …" → bộ phim <b>Super Size Me</b>.')
# dh9 – generation gap at work
M('dh9', '2425', 'Which of the following can be the best title for the passage?', 'The Impact of Technology on Business Practices|The Generation Gap in Such a Technological Era|Managing and Motivating Multi-Generational Workforce|The Generation Gap and Its Effect on Leadership Styles', 'C', 'Bài đề cập sự khác biệt thế hệ ở nơi làm việc (công nghệ, kỳ vọng công việc, phong cách lãnh đạo, giao tiếp) – ý bao quát nhất là về lực lượng lao động nhiều thế hệ → <b>C</b>. A, D chỉ là một khía cạnh.')
N('dh9 (2425 minh hoạ #29, title): các tiêu đề đều chưa hoàn toàn khớp; chọn C (bao quát nhất) – hơi mơ hồ.')
M('dh9', '2425', 'According to the passage, the younger generation ______.', 'prefer hierarchical structures in the workplace.|value input from all levels of the organization.|prioritize traditional career paths.|communicate primarily through traditional channels.', 'B', '"younger generations often prefer collaborative and inclusive leadership styles, valuing input from all levels" → <b>B</b>.')
M('dh9', '2425', 'The word "they" in the first paragraph refers to ______.', 'younger generations|Gen Z|technology|digital age', 'A', '"Younger generations, such as Millennials and Generation Z … <u>They</u> readily embrace new tools" → <b>younger generations</b>.')
M('dh9', '2425', 'The word "thrive" in paragraph 2 is closest in meaning to ______.', 'explode|shrink|succeed|fail', 'C', '<b>thrive</b> = phát triển mạnh ≈ <b>succeed</b>.')
M('dh9', '2425', 'Which of the following is not true according to the passage?', 'Younger generations are more comfortable with technology.|Older generations prioritize flexibility and work-life balance.|Leadership styles vary between generations.|Communication preferences have evolved over the years.', 'B', 'Chính <b>thế hệ trẻ</b> mới ưu tiên sự linh hoạt và cân bằng công việc–cuộc sống; thế hệ lớn tuổi coi trọng sự ổn định → B sai.')
# dh10 – Coca-Cola
M('dh10', '2425', 'Which of the following would be the best title for the reading?', 'The Invention & History of Coca-Cola.|Cola is the World\'s Most Popular Soft Drink|John Pemberton created Coca-Cola.|The Temperance Movement & Coke\'s success', 'A', 'Bài kể về sự ra đời và lịch sử thành công của Coca-Cola → <b>A</b>.')
M('dh10', '2425', 'From paragraph 1, we can see that the American South is ______.', 'short of soft drinks|well-known for its food|not home for famous the drink brand|hot and humid', 'D', '"the birthplace of cola was the hot and humid American South" → <b>hot and humid</b>. (Đề gốc ghi nhầm "South America".)')
N('dh10 (2425 minh hoạ #35): đề ghi "South America", đã sửa thành "the American South" theo bài; đáp án D.')
M('dh10', '2425', 'In paragraph 2, the word "he" refers to ______.', 'Coca-Cola|Pemberton|the American|the French', 'B', '"Deciding that … would look well in advertising, <u>he</u> named it Coca-Cola" → <b>Pemberton</b>.')
M('dh10', '2425', 'In paragraph 3, the word "outlawed" is opposite in meaning to ______.', 'made illegal|taken to court|made legal|allowed', ['C', 'D'], '<b>outlawed</b> = bị cấm (làm cho bất hợp pháp) ↔ <b>made legal</b> hoặc <b>allowed</b>.')
N('dh10 (2425 minh hoạ #37 outlawed): made legal (C) và allowed (D) đều trái nghĩa → chấp nhận C, D.')
M('dh10', '2425', 'All of the following are true of Pemberton EXCEPT that ______.', 'he made “French wine of Coca” from the coca leaf|he combined the coca leaf and cola nut to make “French wine”|he produced stimulating alcohol from coca leaves and cola nuts|he made “French wine of Coca” from the cola nut', ['C', 'D'], 'Pemberton phản đối rượu và làm "French Wine of Coca" từ lá coca; sau đó mới kết hợp lá coca với hạt cola để tạo Coca-Cola (không phải rượu). C (làm rượu từ coca và cola) hoàn toàn sai; D (làm từ hạt cola) cũng sai. Chấp nhận C, D.')
N('dh10 (2425 minh hoạ #38 EXCEPT): C và D đều không đúng với bài → chấp nhận C, D; B cũng chưa chính xác về trình tự.')
M('dh10', '2425', 'In paragraph 3, the word "caught on" is closest in meaning to ______.', 'became popular|became important|became legal|became successful', 'A', '<b>catch on</b> = trở nên phổ biến, được ưa chuộng ≈ <b>became popular</b>.')
M('dh10', '2425', 'Which of the following is responsible for Coke\'s additional success?', 'The temperance movement|Its attracting name|Pemberton\'s good business sense|Coca-Cola\'s great taste', 'A', '"The drink enjoyed additional success since there was a large and popular temperance movement" → <b>A</b>.')

# ======================================================================================
# VIẾT LẠI CÂU
# ======================================================================================
def RW(g, s, a, b, ans, exp):
    F(g, s, a + '<br>' + b + ' {_}', ans, exp)


# ---- vi1: thì
RW('vi1', '2324', 'I have not met her for three years.', 'The last time', ['I met her was three years ago', 'I met her was 3 years ago'], 'Cấu trúc: S + have/has not + V3 + for + khoảng thời gian = <b>The last time + S + V2 + was + khoảng thời gian + ago</b>. Đáp án: The last time <b>I met her was three years ago</b>.')
RW('vi1', '2324', 'I have not seen her since 2000.', 'The last time', ['I saw her was in 2000', 'I saw her was 2000'], 'S + have not + V3 + since + mốc = The last time + S + V2 + was + (in) mốc. Đáp án: The last time <b>I saw her was in 2000</b>.')
RW('vi1', '2324', 'This is the first time I have attended such an enjoyable wedding party.', 'I', ['have never attended such an enjoyable wedding party before', 'have not attended such an enjoyable wedding party before', "haven't attended such an enjoyable wedding party before", 'had never attended such an enjoyable wedding party before'], 'This is the first time + S + have V3 = <b>S + have never + V3 … before</b>. Đáp án: I <b>have never attended such an enjoyable wedding party before</b>.')
RW('vi1', '2324', 'This is the first time I have been abroad.', 'I', ['have never been abroad before', 'have not been abroad before', "haven't been abroad before"], 'This is the first time + S + have V3 = S + have never + V3 … before. Đáp án: I <b>have never been abroad before</b>.')
RW('vi1', '2324', 'My student hasn\'t come to such a big city as Seoul before.', 'This is the first time', ['my student has come to such a big city as Seoul', 'my student has been to such a big city as Seoul', 'my student has come to a big city like Seoul'], 'S + hasn\'t + V3 + before = This is the first time + S + has/have + V3. Đáp án: This is the first time <b>my student has come to such a big city as Seoul</b>.')
RW('vi1', '2324', 'Her children haven\'t joined such an attractive party like that before.', 'This is the first time', ['her children have joined such an attractive party', 'her children have joined such an attractive party like that', 'her children have joined an attractive party like that'], 'This is the first time + S + have V3. Đáp án: This is the first time <b>her children have joined such an attractive party</b>.')
RW('vi1', 'tn', 'This is the first time he went abroad.', 'He', ['has never been abroad before', 'has not been abroad before', "hasn't been abroad before", 'has never gone abroad before'], 'This is the first time + S + has V3 → S + has never + V3 + before. (Đề gốc dùng "went"; dạng chuẩn là "has been/gone abroad".) Đáp án: He <b>has never been abroad before</b>.')
RW('vi1', 'tn', 'She started to learn driving 1 month ago.', 'She', ['has learnt driving for 1 month', 'has learned driving for 1 month', 'has been learning driving for 1 month', 'has learnt to drive for a month', 'has learned to drive for one month', 'has been learning to drive for 1 month'], 'Started … 1 month ago → hiện tại hoàn thành + <b>for 1 month</b>. Đáp án: She <b>has learnt (been learning) to drive for 1 month</b>.')
RW('vi1', 'tn', 'We began eating when it started to rain.', 'We', ['have been eating since it started to rain', 'have eaten since it started to rain', 'have been eating since it began to rain'], 'Mốc bắt đầu: when it started → <b>since it started to rain</b> + hiện tại hoàn thành (tiếp diễn). Đáp án: We <b>have been eating since it started to rain</b>.')
RW('vi1', 'tn', 'I last had my hair cut when I left her.', 'I haven\'t', ['had my hair cut since I left her', 'had my hair cut since i left her'], 'last … when = hiện tại hoàn thành phủ định + since. Đáp án: I haven\'t <b>had my hair cut since I left her</b>.')
RW('vi1', 'tn', 'It is a long time since we last met.', 'We', ['have not met for a long time', "haven't met for a long time", "haven't seen each other for a long time", 'have not seen each other for a long time'], 'It is a long time since + S + last + V2 = S + haven\'t + V3 + for a long time. Đáp án: We <b>haven\'t met for a long time</b>.')
RW('vi1', 'tn', 'I haven\'t cheated in exam for years.', 'It is', ['years since i last cheated in an exam', 'years since i cheated in an exam', 'years since i last cheated in exam', 'years since i cheated in exam', 'years since i last cheated in exams'], 'S + haven\'t + V3 + for + khoảng thời gian = It is + khoảng thời gian + since + S + (last) + V2. Đáp án: It is <b>years since I last cheated in an exam</b>.')
RW('vi1', 'tn', 'How long has she lived in Danang?', 'When', ['did she start living in danang', 'did she begin living in danang', 'did she move to danang', 'did she start to live in danang', 'did she begin to live in danang', 'did she come to danang'], 'How long + hiện tại hoàn thành ↔ <b>When did + S + start/begin + V-ing</b>. Đáp án: When <b>did she start living in Danang</b>?')
RW('vi1', 'tn', 'He hasn\'t smoked for 2 years.', 'He last', ['smoked 2 years ago', 'smoked two years ago'], 'S + hasn\'t + V3 + for + khoảng thời gian = S + last + V2 + khoảng thời gian + ago. Đáp án: He last <b>smoked 2 years ago</b>.')
RW('vi1', 'tn', 'I have learnt French for 3 years.', 'I', ['started learning french 3 years ago', 'began learning french 3 years ago', 'started to learn french 3 years ago', 'began to learn french 3 years ago', 'started learning french three years ago', 'began learning french three years ago', 'started to learn french three years ago', 'began to learn french three years ago'], 'have + V3 + for 3 years = started/began + V-ing + 3 years ago. Đáp án: I <b>started learning French 3 years ago</b>.')
RW('vi1', 'tn', 'I haven\'t met her for 5 days.', 'The last time', ['i met her was 5 days ago', 'i met her was five days ago'], 'The last time + S + V2 + was + khoảng thời gian + ago. Đáp án: The last time <b>I met her was 5 days ago</b>.')
RW('vi1', '2425', 'Mr. Minh started working at this office 5 years ago.', 'Mr. Minh has', ['worked at this office for 5 years', 'worked at this office for five years', 'been working at this office for 5 years', 'been working at this office for five years'], 'started … 5 years ago → hiện tại hoàn thành + for 5 years. Đáp án: Mr. Minh has <b>worked (been working) at this office for 5 years</b>.')
RW('vi1', '2425', 'The last time I had a business meeting with him was in February.', 'I have', ['not had a business meeting with him since february', "haven't had a business meeting with him since february"], 'The last time + S + V2 + was + mốc = S + haven\'t + V3 + since + mốc. Đáp án: I have <b>not had a business meeting with him since February</b>.')
RW('vi1', '2425', 'I last saw her when I was a student 2 years ago.', 'I have', ['not seen her for 2 years', 'not seen her for two years', "never seen her for 2 years"], 'last … 2 years ago = haven\'t + V3 + for 2 years. Đáp án: I have <b>not seen her for 2 years</b>.')
RW('vi1', '2425', 'I haven\'t heard him since August.', 'The last', ['time i heard from him was in august', 'time i heard him was in august', 'time i heard of him was in august', 'time i heard from him was august'], 'S + haven\'t + V3 + since + mốc = The last time + S + V2 + was + (in) mốc. Đáp án: The last <b>time I heard from him was in August</b>.')

# ---- vi2: động từ khuyết thiếu
RW('vi2', '2324', 'If I were you, I would spend more time talking with my children. (should)', 'You', ['should spend more time talking with your children', 'should spend more time talking to your children'], 'If I were you, I would … = <b>You should …</b>. Đáp án: You <b>should spend more time talking with your children</b>.')
RW('vi2', '2324', 'If I were you, I would write to him. (should)', 'You', ['should write to him'], 'If I were you, I would … = You should …. Đáp án: You <b>should write to him</b>.')
RW('vi2', '2324', 'John doesn\'t get permission to use that computer. (mustn\'t)', 'John', ["mustn't use that computer", 'must not use that computer'], 'Không được phép = <b>mustn\'t</b> + V. Đáp án: John <b>mustn\'t use that computer</b>.')
RW('vi2', '2324', 'She doesn\'t get permission to go out at night. (mustn\'t)', 'She', ["mustn't go out at night", 'must not go out at night'], 'Đáp án: She <b>mustn\'t go out at night</b>.')
RW('vi2', '2324', 'Every staff isn\'t allowed to smoke or eat in the office. (using a modal verb)', 'Staff', ["mustn't smoke or eat in the office", 'must not smoke or eat in the office', "can't smoke or eat in the office", 'cannot smoke or eat in the office'], 'not allowed to = mustn\'t. Đáp án: Staff <b>mustn\'t smoke or eat in the office</b>.')
RW('vi2', '2324', 'You are not allowed to take photographs in the museum. (using a modal verb)', 'You', ["mustn't take photographs in the museum", 'must not take photographs in the museum', "can't take photographs in the museum", 'cannot take photographs in the museum', "mustn't take photos in the museum"], 'Đáp án: You <b>mustn\'t take photographs in the museum</b>.')
RW('vi2', '2324', 'It is not necessary for Jack to call Ben today. (using a modal verb)', 'Jack', ["doesn't have to call ben today", "needn't call ben today", 'need not call ben today', 'does not have to call ben today'], 'It is not necessary for S to V = S <b>needn\'t</b> V / S <b>doesn\'t have to</b> V. Đáp án: Jack <b>needn\'t call Ben today</b>.')
RW('vi2', '2324', 'It is not necessary for John to water these flowers. (using a modal verb)', 'John', ["doesn't have to water these flowers", "needn't water these flowers", 'need not water these flowers', 'does not have to water these flowers'], 'Đáp án: John <b>doesn\'t have to / needn\'t water these flowers</b>.')
RW('vi2', '2324', 'It would not be good for your classmate to use his smartphone during the lesson.', 'Your classmate shouldn\'t', ['use his smartphone during the lesson', 'use his smartphone in the lesson'], 'It would not be good for S to V = S shouldn\'t V. Đáp án: Your classmate shouldn\'t <b>use his smartphone during the lesson</b>.')
RW('vi2', '2324', 'Customers are advised to check their luggage before leaving the airport.', 'Customers should', ['check their luggage before leaving the airport'], 'be advised to V = should V. Đáp án: Customers should <b>check their luggage before leaving the airport</b>.')
RW('vi2', 'tn', 'I\'d advise you to tell the truth to your family.', 'You', ['should tell the truth to your family', 'ought to tell the truth to your family'], 'I\'d advise you to … = You should …. Đáp án: You <b>should tell the truth to your family</b>.')
RW('vi2', 'tn', 'It is not necessary for us to wear uniforms every day.', 'We', ["don't have to wear uniforms every day", "needn't wear uniforms every day", 'do not have to wear uniforms every day', 'need not wear uniforms every day'], 'not necessary = don\'t have to / needn\'t. Đáp án: We <b>don\'t have to wear uniforms every day</b>. (Đề gốc bắt đầu bằng "I" – đã sửa thành "We" cho khớp nghĩa.)')
N('vi2 (tn Transformation a #2): nguồn gợi ý bắt đầu bằng "I" nhưng câu gốc nói về "us" → đổi thành "We".')
RW('vi2', 'tn', 'We aren\'t allowed to drive without wearing a helmet.', 'We', ["mustn't drive without wearing a helmet", 'must not drive without wearing a helmet', "can't drive without wearing a helmet", 'cannot drive without wearing a helmet'], 'not allowed to = mustn\'t. Đáp án: We <b>mustn\'t drive without wearing a helmet</b>.')
RW('vi2', 'tn', 'It is necessary for young people to plan their future career carefully.', 'Young people', ['must plan their future career carefully', 'have to plan their future career carefully', 'need to plan their future career carefully', 'should plan their future career carefully'], 'It is necessary for S to V = S must / have to / need to V. Đáp án: Young people <b>must plan their future career carefully</b>.')
RW('vi2', 'tn', 'It is very important for us to do well at school.', 'We', ['must do well at school', 'have to do well at school', 'should do well at school', 'need to do well at school'], 'It is very important for S to V = S must / should V. Đáp án: We <b>must do well at school</b>.')
RW('vi2', '2425', 'It would be a good idea for you to share the housework with your mother.', 'You', ['should share the housework with your mother', 'ought to share the housework with your mother'], 'It would be a good idea for you to … = You should …. Đáp án: You <b>should share the housework with your mother</b>.')
RW('vi2', '2425', 'They don\'t allow students to cheat in the exam.', 'Students', ["mustn't cheat in the exam", 'must not cheat in the exam', "aren't allowed to cheat in the exam", 'are not allowed to cheat in the exam', "can't cheat in the exam", 'cannot cheat in the exam'], 'Chủ động → bị động/khuyết thiếu: Students <b>aren\'t allowed to cheat / mustn\'t cheat</b> in the exam.')
RW('vi2', '2425', 'It is not necessary for Nancy to clean the flat. (need)', 'Nancy', ["needn't clean the flat", 'need not clean the flat', "doesn't need to clean the flat", 'does not need to clean the flat'], 'Dùng <b>need</b> như khuyết thiếu (phủ định): Nancy <b>needn\'t clean the flat</b>.')
RW('vi2', '2425', 'I am sure you were surprised when you heard all the news. (must)', 'You', ['must have been surprised when you heard all the news', 'must have been surprised when you heard the news'], '<b>must have + V3</b> = chắc hẳn đã (suy đoán chắc chắn về quá khứ). Đáp án: You <b>must have been surprised when you heard all the news</b>.')
RW('vi2', '2425', 'The police let him leave after they had questioned him.', 'The police allowed', ['him to leave after they had questioned him'], 'let sb V = allow sb to V. Đáp án: The police allowed <b>him to leave after they had questioned him</b>.')

# ---- vi3: viết câu từ gợi ý (open)
O('vi3', '2324', 'Drink / lots / water / be / good / our health.', 'Đáp án mẫu: <b>Drinking lots of water is good for our health.</b>')
O('vi3', '2324', 'Watch / much / TV / not / good / your eyes.', 'Đáp án mẫu: <b>Watching too much TV is not good for your eyes.</b>')
O('vi3', '2324', 'Do / exercise / regular / help / you / stay / healthy.', 'Đáp án mẫu: <b>Doing exercise regularly helps you stay healthy.</b>')
O('vi3', '2324', 'Eat / healthy / be / important / part / maintain / good / health.', 'Đáp án mẫu: <b>Eating healthily is an important part of maintaining good health.</b>')
O('vi3', '2324', 'Build / smart city / seem / impossible / everyone 50 years / ago.', 'Đáp án mẫu: <b>Building a smart city seemed impossible to everyone 50 years ago.</b> (seem + tính từ; dùng quá khứ vì có "50 years ago")')
O('vi3', '2324', 'I / not think / live / in a smart city / good / everyone.', 'Đáp án mẫu: <b>I don\'t think living in a smart city is good for everyone.</b> (think là động từ trạng thái, không dùng tiếp diễn)')
O('vi3', '2324', 'Poverty / overcrowding / ruin / life / people / many big cities.', 'Đáp án mẫu: <b>Poverty and overcrowding ruin the life of people in many big cities.</b>')
O('vi3', '2324', 'Due / poverty / overcrowding, / life / people / many big cities / ruin.', 'Đáp án mẫu: <b>Due to poverty and overcrowding, the life of people in many big cities is ruined.</b> (bị động)')

# ---- vi4: viết đoạn
O('vi4', '2223', 'Topic 1: Think of something that happened to you or another person. Write an online posting of 140–160 words. You can write about: what happened, when and where, and who was involved; how you and the other felt; your wish.',
  '<b>Bài mẫu:</b> <i>Last Sunday, my best friend Lan and I went to the city library to prepare for our English test. At about 4 p.m., Lan suddenly realised that she had lost her wallet with her student card inside. She felt really worried and almost cried. I felt sorry for her, so we retraced our steps and asked the librarian for help. Fortunately, a boy had found the wallet near the entrance and handed it in. Lan thanked him warmly and we were both relieved. I felt happy that honest people still exist. I wish everyone would be careful with their belongings, and I hope that the boy will always be rewarded for his kindness.</i><br>Gợi ý: nêu rõ <b>what/when/where/who</b>, cảm xúc (worried, relieved), ước muốn (I wish …) bằng thì quá khứ đơn, khoảng 140–160 từ.')
O('vi4', '2223', 'Topic 2: Write a paragraph about the benefits of being independent and how to become independent. (What are the benefits? How can someone be more independent?)',
  '<b>Bài mẫu:</b> <i>Being independent has many benefits for teenagers. Firstly, independent people can make their own decisions and solve problems without relying on others, so they become more confident and responsible. Secondly, they learn useful life skills such as time management and housekeeping, which help them live well on their own in the future. To become more independent, teenagers should start with small tasks like doing the housework, managing their pocket money and planning their study schedule. They should also learn to think carefully before making decisions and accept the results. In short, independence helps us grow up and prepare for adult life.</i>')
O('vi4', '2223', 'Topic 3: Write a paragraph about your family rules and give some reasons. (What are the family rules? Why do your parents set these rules? How do you feel when you have to obey these rules?)',
  '<b>Bài mẫu:</b> <i>There are several rules in my family. First, I must be home before 9 p.m. and I mustn\'t use my phone during meals. Second, I have to do my homework before watching TV, and I ought to help my mother with the housework at weekends. My parents set these rules because they want me to stay safe, study well and become responsible. At first I felt a little uncomfortable, but now I understand that the rules are for my own good, so I always try to obey them.</i> (Dùng modal verbs: must, mustn\'t, have to, ought to.)')
O('vi4', '2324', 'A new fitness club has just opened near your school. Write a short message (30–45 words) to your friend. In your message, you should: tell him/her about the club; suggest that he/she should join the club with you; ask if he/she prefers to go with you in the morning or afternoon.',
  '<b>Bài mẫu:</b> <i>Hi Nam, a new fitness club has just opened near our school. It has a gym and a swimming pool. You should join it with me! Do you prefer to go with me in the morning or in the afternoon? Let me know soon. Bye!</i>')
O('vi4', '2324', 'Write an opinion essay (80–100 words) stating the opposite view about the topic: "Parents should strictly limit their children\'s screen time." Suggested ideas: parents limit what teens can benefit from it; the gap between parents and children may become wider.',
  '<b>Bài mẫu:</b> <i>I disagree that parents should strictly limit their children\'s screen time. Firstly, teenagers can benefit a lot from screens: they can learn online, research for school projects and keep in touch with friends. Strict limits would take these benefits away. Secondly, too many rules may make the gap between parents and children wider, because teenagers feel they are not trusted and may hide what they do. Instead of banning screens, parents should talk with their children, agree on reasonable time and guide them to use technology safely.</i>')
O('vi4', '2324', 'Write an article (80–100 words) about other advantages and disadvantages of roof gardens in the city. Ideas: improving air quality; creating habitats for wildlife; interacting and connecting with nature / increasing weight on the structure; being difficult to repair and maintain.',
  '<b>Bài mẫu:</b> <i>Roof gardens bring several advantages to city life. Firstly, they help improve air quality because plants absorb dust and carbon dioxide. They also create habitats for wildlife such as birds and butterflies. Moreover, city dwellers can interact and connect with nature, which reduces stress. However, there are some disadvantages. The gardens increase the weight on the structure of the building, so the roof must be very strong. In addition, they are difficult to repair and maintain. In conclusion, roof gardens are useful but need careful planning.</i>')

# ======================================================================================
# NÓI & GIAO TIẾP
# ======================================================================================
M('gt1', '2425', 'Jim: "Dad, do you mind if I go to my friend\'s birthday party this weekend?" – Father: "______."', 'Of course you can.|Really|Who is coming?|Who has ideas?', 'A', 'Đây là câu xin phép; cách đáp lại phù hợp nhất trong các phương án là đồng ý: <b>Of course you can.</b> (Thường nói chuẩn hơn là "Of course not" khi trả lời "Do you mind if…". Các phương án B, D không hợp ngữ cảnh; C là câu hỏi thêm.)')
N('gt1 (2425 Ex3 #28): với "Do you mind if…?" cách đồng ý chuẩn là "Of course not / No, go ahead"; đề không có nên chọn A (Of course you can).')
O('gt2', 'tn', 'Mum, / can I / go / my friend\'s / birthday party / Saturday evening?', 'Đáp án mẫu: <b>Mum, can I go to my friend\'s birthday party on Saturday evening?</b>')
O('gt2', 'tn', 'it OK / if / I / stay / the night / her house / after / party?', 'Đáp án mẫu: <b>Is it OK if I stay the night at her house after the party?</b>')
O('gt2', 'tn', 'Would / you mind / if / I / open / the windows? / It / too stuffy / in here.', 'Đáp án mẫu: <b>Would you mind if I opened the windows? It\'s too stuffy in here.</b> (Would you mind if + S + V quá khứ đơn)')
O('gt2', 'tn', 'Dad, / you / mind / if / I / color / hair?', 'Đáp án mẫu: <b>Dad, do you mind if I color my hair?</b> (Do you mind if + S + V hiện tại đơn)')
O('gt2', 'tn', 'Mum, / Would / you / mind / if / I / go out / my friends / weekend?', 'Đáp án mẫu: <b>Mum, would you mind if I went out with my friends this weekend?</b>')
O('gt3', '2324', 'Give some unhealthy habits.', 'Gợi ý: <i>Some unhealthy habits are staying up late, eating too much junk food, skipping breakfast, smoking and spending too much time in front of screens.</i>')
O('gt3', '2324', 'Give some healthy habits.', 'Gợi ý: <i>Healthy habits include eating a balanced diet, drinking enough water, doing exercise regularly, getting enough sleep and having regular check-ups.</i>')
O('gt3', '2324', 'How to live a long and healthy life?', 'Gợi ý: <i>To live a long and healthy life, we should eat a balanced diet, work out regularly, sleep at least eight hours, avoid smoking and alcohol, keep a positive attitude and have regular medical check-ups.</i>')
O('gt3', '2324', 'Topic: Give instructions on how to do star jumps.', 'Gợi ý: <i>First, stand straight with your feet together and your arms by your sides. Next, jump up and spread your legs and arms out wide at the same time. Then jump again and bring your feet and arms back to the starting position. Repeat this about ten to twenty times and breathe regularly.</i>')
O('gt3', '2324', 'Topic: Talking about the different generations of your family. (the number of generations in your family; characteristics of your grandparents and your parents; conflicts between you and your grandparents/parents)', 'Gợi ý: <i>There are three generations in my family: my grandparents, my parents and me. My grandparents are traditional and hard-working, while my parents are modern and open-minded. Sometimes my grandparents disagree with me about clothes and screen time, but we solve the conflicts by talking and listening to each other.</i>')
O('gt3', '2324', 'How often do you use a smartphone?', 'Gợi ý: <i>I use my smartphone every day, mostly to chat with friends, look up information for my homework and listen to music – about two hours a day.</i>')
O('gt3', '2324', 'Should parents strictly limit teenagers\' screen time?', 'Gợi ý (đồng ý): <i>I think parents should limit screen time because too much time on screens harms our eyes, sleep and study. (Không đồng ý): It is better to guide teenagers than to ban them.</i>')
O('gt3', '2324', 'Some characteristics of green cities.', 'Gợi ý: <i>Green cities reduce their impact on the environment. City dwellers use public transport such as trams and electric buses, which reduces traffic jams and pollution. They also have lots of parks and use renewable energy.</i>')
O('gt3', '2324', 'Some characteristics of smart cities.', 'Gợi ý: <i>AI technologies such as cameras, robots and smart sensors are installed to help the city operate more effectively, for example controlling traffic and saving energy.</i>')
O('gt3', '2324', 'Disadvantages of living in smart cities?', 'Gợi ý: <i>City dwellers may lose their right to privacy in public areas. It is not easy for some people to get familiar with and use smart devices. People may also feel lonely because there are many AI technologies around them.</i>')
O('gt3', '2324', 'Do you like living in a green city or a smart one? Why?', 'Gợi ý: <i>I prefer a green city because it has fresh air, many trees and less noise, which is better for health. However, a smart city is also convenient because technology makes life easier.</i>')


# ======================================================================================
# LOẠI TRÙNG
# ======================================================================================
def strip_tags(s):
    s = re.sub(r'<sup>.*?</sup>', '', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    return re.sub(r'<[^>]+>', '', s)


def nk(s):
    """chuẩn hoá: chữ thường, bỏ khoảng trắng + dấu câu"""
    return re.sub(r'[\W_]+', '', strip_tags(s).lower())


def sig(it):
    if it['t'] == 'mcq':
        opts = sorted(nk(o) + '~' + nk(''.join(re.findall(r'<u>(.*?)</u>', o))) for o in it['o'])
        return nk(it['q']), opts
    return nk(it['q']), [nk(it.get('hint') or '')]


def is_dup(a, b):
    if a['t'] != b['t']:
        return False
    qa, oa = sig(a)
    qb, ob = sig(b)
    if qa == qb and oa == ob:
        return 'exact'
    if a['t'] == 'open' and qa == qb:
        return 'exact'
    if len(qa) < 18 or len(qb) < 18:
        return False
    r = difflib.SequenceMatcher(None, qa, qb).ratio()
    if a['t'] == 'mcq':
        sa = set(x.split('~')[0] for x in oa)
        sb = set(x.split('~')[0] for x in ob)
        j = len(sa & sb) / max(1, len(sa | sb))
        if r >= 0.88 and j >= 0.6:
            return 'fuzzy'
    elif a['t'] == 'fill' and r >= 0.97:
        return 'fuzzy'
    return False


KEPT = []
REMOVED = []      # (src, gid, q, kept_src, kind)
for it in RAW:
    d = None
    for k in KEPT:
        kind = is_dup(it, k)
        if kind:
            d = (k, kind)
            break
    if d:
        REMOVED.append((it['s'], it['g'], strip_tags(it['q'])[:70] or strip_tags(it['o'][0])[:40], d[0]['s'], d[1]))
    else:
        KEPT.append(it)

# ======================================================================================
# GÁN ID
# ======================================================================================
cnt = {}
for it in KEPT:
    cnt[it['g']] = cnt.get(it['g'], 0) + 1
    it['id'] = '%s.%d' % (it['g'], cnt[it['g']])


def item_out(it, nid=None):
    o = {'id': nid or it['id'], 't': it['t'], 'q': it['q']}
    if it['t'] == 'mcq':
        o['o'] = list(it['o'])
    if it.get('hint'):
        o['hint'] = it['hint']
    return o


def pick(lst, k):
    n = len(lst)
    return [lst[int((i + 0.5) * n / k)] for i in range(k)]


by = {}
for it in KEPT:
    by.setdefault(it['g'], []).append(it)

# ======================================================================================
# BÀI KIỂM TRA 40 CÂU (bản sao, id kt.N)
# ======================================================================================
sel = []   # (group_kt, item)
sel_pa = pick(by['pa1'], 2) + pick(by['pa2'], 2)
sel_tv = pick(by['tv1'], 6) + pick(by['tv2'], 2) + pick(by['tv3'], 2)
sel_ng = pick(by['ng1'], 3) + pick(by['ng2'], 3) + pick(by['ng3'], 5) + pick(by['er1'], 5)
sel_dt = by['dt5'][:5]
sel_dh = by['dh7'][:5]
KT_GROUPS = [
    ('kt1', 'Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation, or the word that differs in the position of primary stress.', '', sel_pa),
    ('kt2', 'Mark the letter A, B, C, or D to indicate the correct answer (từ vựng; đồng nghĩa; trái nghĩa).', '', sel_tv),
    ('kt3', 'Mark the letter A, B, C, or D to indicate the correct answer / the underlined part that needs correction (ngữ pháp).', '', sel_ng),
    ('kt4', 'Read the following passage and choose the best option to fill in each blank.', GROUPS['dt5']['passage'], sel_dt),
    ('kt5', 'Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each question.', GROUPS['dh7']['passage'], sel_dh),
]
KT = []
n = 0
kt_groups_out = []
for gid, instr, passage, its in KT_GROUPS:
    outs = []
    for it in its:
        n += 1
        c = dict(it)
        c['id'] = 'kt.%d' % n
        KT.append(c)
        outs.append(item_out(c))
    kt_groups_out.append({'id': gid, 'instr': instr, 'passage': passage, 'items': outs})
assert n == 40, n

# ======================================================================================
# LÝ THUYẾT
# ======================================================================================
exec(open(os.path.join(ROOT, 'tools/gen_mt1_ontap_theory.py'), encoding='utf8').read())

# ======================================================================================
# GHI FILE
# ======================================================================================
pages = []
for pid, title in PAGES:
    gs = []
    for gid, g in GROUPS.items():
        if g['page'] != pid:
            continue
        its = [item_out(x) for x in by.get(gid, [])]
        if not its:
            continue
        gd = {'id': gid, 'instr': g['instr']}
        if g['passage']:
            gd['passage'] = g['passage']
        if g['note']:
            gd['note'] = g['note']
        if g['bank']:
            gd['bank'] = g['bank']
        gd['items'] = its
        gs.append(gd)
    pages.append({'id': pid, 'title': title, 'mode': 'practice', 'groups': gs})
pages.append({'id': 'kiem-tra', 'title': 'Kiểm tra tổng hợp (40 câu)', 'mode': 'test', 'minutes': 45, 'groups': kt_groups_out})

SET = {'id': 'lop11-mt1-ontap', 'title': 'Ôn tập đề cương – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': THEORY, 'pages': pages}

with open(os.path.join(ROOT, 'units/mt1_ontap.py'), 'w', encoding='utf8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""Dữ liệu SET – Ôn tập đề cương Mid-term 1 (gộp dc2223, dc2324, dc2425, tn). Sinh bởi tools/gen_mt1_ontap.py.\nĐáp án + giải thích: units/mt1_ontap_dapan.py."""\n\nSET = ')
    f.write(pprint.pformat(SET, width=160, sort_dicts=False) + '\n')

ANS, EXP = {}, {}
for it in KEPT + KT:
    if it['t'] != 'open':
        ANS[it['id']] = it['ans']
    EXP[it['id']] = it['exp']
with open(os.path.join(ROOT, 'units/mt1_ontap_dapan.py'), 'w', encoding='utf8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""Đáp án + giải thích – Ôn tập đề cương Mid-term 1 (Tiếng Anh 11 Global Success).\n'
            'Nguồn Word (dc2223, dc2324, dc2425, tn) KHÔNG có khoá đáp án => toàn bộ đáp án tự giải độc lập.\n'
            'Quy ước: mcq: chữ cái (list = nhiều đáp án đều đúng); fill: list đáp án chấp nhận hoặc {"blanks": [[..],[..]]}; open: chỉ có EXPLANATIONS (đáp án mẫu)."""\n\n')
    f.write('GHI_CHU_RA_SOAT = ' + pprint.pformat(GHI, width=160) + '\n\n')
    f.write('ANS = ' + pprint.pformat(ANS, width=160, sort_dicts=False) + '\n\n')
    f.write('EXPLANATIONS = ' + pprint.pformat(EXP, width=160, sort_dicts=False) + '\n')

# ---- thống kê
orig = {}
for it in RAW:
    orig[it['s']] = orig.get(it['s'], 0) + 1
rem = {}
for r in REMOVED:
    rem[r[0]] = rem.get(r[0], 0) + 1
print('Câu gốc đã khai báo theo nguồn:', orig, 'tổng', len(RAW))
print('Bỏ trùng theo nguồn:', rem, 'tổng', len(REMOVED))
print('Còn lại theo page:')
for p in pages:
    print('  %-14s %d' % (p['id'], sum(len(g['items']) for g in p['groups'])))
print('Tổng còn lại (không tính kiểm tra):', len(KEPT))
for r in REMOVED:
    print('  DUP [%s] %s -> giữ của %s (%s): %s' % (r[0], r[1], r[3], r[4], r[2]))
