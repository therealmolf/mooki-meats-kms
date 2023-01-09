--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: emp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emp (
    emp_id integer NOT NULL,
    emp_name character varying(255) NOT NULL,
    team_name character varying(25),
    role_name character varying(25) NOT NULL,
    ssn character varying(11) NOT NULL,
    degree character varying(255),
    emp_desc text,
    date_hired date,
    emp_delete_ind boolean
);


ALTER TABLE public.emp OWNER TO postgres;

--
-- Name: emp_emp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.emp_emp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emp_emp_id_seq OWNER TO postgres;

--
-- Name: emp_emp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.emp_emp_id_seq OWNED BY public.emp.emp_id;


--
-- Name: emp_know; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emp_know (
    emp_id integer NOT NULL,
    know_id integer NOT NULL,
    emp_know_delete_ind boolean
);


ALTER TABLE public.emp_know OWNER TO postgres;

--
-- Name: emp_know_emp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.emp_know_emp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emp_know_emp_id_seq OWNER TO postgres;

--
-- Name: emp_know_emp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.emp_know_emp_id_seq OWNED BY public.emp_know.emp_id;


--
-- Name: emp_know_know_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.emp_know_know_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emp_know_know_id_seq OWNER TO postgres;

--
-- Name: emp_know_know_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.emp_know_know_id_seq OWNED BY public.emp_know.know_id;


--
-- Name: knowledge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.knowledge (
    know_id integer NOT NULL,
    know_type character varying(30) NOT NULL,
    know_name character varying(255) NOT NULL,
    know_desc text NOT NULL,
    prop_date timestamp without time zone,
    prop_by character varying(255),
    app_status character varying(13),
    know_delete_ind boolean
);


ALTER TABLE public.knowledge OWNER TO postgres;

--
-- Name: knowledge_know_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.knowledge_know_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.knowledge_know_id_seq OWNER TO postgres;

--
-- Name: knowledge_know_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.knowledge_know_id_seq OWNED BY public.knowledge.know_id;


--
-- Name: team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team (
    team_name character varying(25) NOT NULL,
    team_desc text NOT NULL
);


ALTER TABLE public.team OWNER TO postgres;

--
-- Name: emp emp_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp ALTER COLUMN emp_id SET DEFAULT nextval('public.emp_emp_id_seq'::regclass);


--
-- Name: emp_know emp_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp_know ALTER COLUMN emp_id SET DEFAULT nextval('public.emp_know_emp_id_seq'::regclass);


--
-- Name: emp_know know_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp_know ALTER COLUMN know_id SET DEFAULT nextval('public.emp_know_know_id_seq'::regclass);


--
-- Name: knowledge know_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.knowledge ALTER COLUMN know_id SET DEFAULT nextval('public.knowledge_know_id_seq'::regclass);


--
-- Data for Name: emp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.emp (emp_id, emp_name, team_name, role_name, ssn, degree, emp_desc, date_hired, emp_delete_ind) FROM stdin;
4	Jessica Smith	Hydration	Developer	23010972337	BS Industrial Engineering	Public base short. Admit would administration possible machine. Chance consumer boy address main who ask. Treatment attention push middle animal station as.	1973-09-08	\N
5	Jonathan Jones	Cooking	Staff	77935646955	BS Industrial Engineering	Agree get book morning. Law indicate production American even.\nSingle let none share. Game staff live situation likely stage think.	1996-11-23	\N
6	Steven Lara	Packaging	Staff	55296910526	BS Computer Science	Stop society voice your figure leave one. Read we big create.\nDoor something use day threat inside weight. Few spend move matter significant. Line catch answer close certain national research.	2015-12-01	\N
7	Shannon Choi	Coating	Engineer	18265091409	BS Management	Tv instead rate suggest stuff behavior employee improve. Everybody box heart degree respond onto appear. Discussion make herself able lose fear.	2010-01-06	\N
8	Gregory Mullins	Cooling	Staff	29932891494	BS Economics	Race on none week none. Sport everything move own fund free fly.\nService operation nature station. Head that house professor analysis.\nWrong middle its middle. Such whatever end magazine.	2011-07-10	\N
9	Jill Watson	TVP	Technician	3858481433	BS Management	Though page audience direction sort get. Ready here manage appear large bag fall. Challenge quality practice realize some ten.	1988-02-07	\N
10	Kyle Grimes	Cooking	Technician	75475292797	BS Food Science	Order Mr focus guy unit Republican poor. Yard college about win receive dream kitchen. Government score spend important.	1994-02-27	\N
11	Scott Jacobs	TVP	Technician	24618091081	BS Computer Science	Watch truth blue speech leg away. Part from help reason. Enough citizen product own and.\nFollow film or its officer quite. Win across others TV travel region.	2018-11-16	\N
12	Amy Velasquez	Hydration	Technician	24553657247	BS Economics	Here site down few message who mind. South radio few show son may central. Into month understand behind music from.\nTest sister issue sea everything. Cold society discover economic at stay.	2017-07-06	\N
13	Tammy Chavez	ESLP	Staff	70081246689	BS Food Science	Information among hot whatever concern company. Tree return skin security.\nMention almost environmental maybe. Meet song role adult and water.\nThird discuss performance office throw.	2011-03-31	\N
14	Mr. Christopher Lucas DDS	ESLP	Staff	7227147698	BS Economics	Street safe now friend. Remain also soon watch modern image new.\nPrepare million movie pretty beyond bed. By talk authority popular which street loss. As owner sister think.	1993-04-28	\N
15	Anita Townsend	Coating	Technician	52337457221	BS Food Science	Admit base success newspaper generation. Staff particular adult lay design give free hold.\nCan later relationship. Benefit entire citizen peace.	1978-12-11	\N
16	Melissa Berg	Cooling	Staff	118026068	BS Management	Find far choice plan who lay end hard. Trade point sister.\nAlso pass couple stay wind present put.\nYou night his evening view power. Whatever place free crime.	1979-01-10	\N
17	Eric Watson	Packaging	Technician	94142339997	BS Industrial Engineering	Development new thousand through buy. Result nice computer last. Late clearly lay make program. Around feeling deep.\nVisit often country with thank health. Congress much similar appear drop.	2017-03-15	\N
18	Patrick Rice	ESLP	Assistant	18680048549	BS Computer Science	Run either what range continue part always. Sing forget guess set join serious. Play mind black food under.\nWill heavy image agree develop positive nor. Old mind hair there.\nA state people purpose.	2013-08-06	\N
19	Adam Hamilton	ESLP	Assistant	34052676551	BS Food Science	That others imagine cold because those dog ok.\nBelieve across PM hundred himself natural country central. Full understand within ball.	2015-09-23	\N
20	Nathan Hodge	Cooking	Engineer	81596074128	BS Computer Science	Read your expert book memory make. Foot black control so blood improve fact. Me open evening next necessary another security.	1972-10-09	\N
21	Taylor Coleman	Hydration	Assistant	1488120881	BS Food Science	Prepare fear enough respond. Well spend fact show me support state garden.\nOperation major marriage realize soon fact information. Alone model final themselves charge.	2017-07-25	\N
22	David Villanueva	ESLP	Assistant	85282659160	BS Industrial Engineering	Crime east but them seven. Mission candidate notice fast firm.\nDown set nation itself care fish catch source. Gas direction born moment put loss. Debate party hospital gun process.	1976-05-25	\N
23	Andrea Robbins	Hydration	Technician	81971664037	BS Industrial Engineering	Control recent baby seem send. Air fight letter notice when interesting book close.\nGlass no age value. Significant pass agent generation class would dog. Prevent thing receive term.	1976-07-08	\N
24	Matthew Boyd	Hydration	Staff	10833331303	BS Food Science	Friend nor however anyone window wrong rate whom. Condition nice group language wear you model turn. Unit mouth quite science soon wind hot.	1992-12-21	\N
25	Amanda Mathis	Cooling	Technician	65210590327	BS Computer Science	Difficult thought region smile material think operation. Race else newspaper couple.\nSee sister hard huge sure. Dream us society entire expect film. Garden week prepare my gun right contain sign.	1977-08-07	\N
26	Alec Valenzuela	Hydration	Engineer	13898469668	BS Industrial Engineering	Suffer record song. Baby event we collection matter ten policy. Show society pretty responsibility.	1979-12-07	\N
27	David Pearson	Coating	Developer	67630153011	BS Food Science	Job air much sign current. Far story professional drop person natural church. Any something better occur thing. Air get case agency.	1995-08-17	\N
28	Eric Mason	Packaging	Engineer	39230636919	BS Industrial Engineering	Simply page scene blood fish my responsibility. Single get matter resource either day since skin. Structure artist growth prevent money clear Republican. Wind which back property audience simple.	1981-02-13	\N
29	Jessica Jones MD	ESLP	Assistant	86226445330	BS Economics	Enough mother guess any son system. Up mission produce need chair investment feeling. Partner board perform difference.	1976-05-15	\N
30	James Hill	Coating	Developer	6064514451	BS Food Science	Father class financial democratic mention simply easy gas. Office left for figure.\nFall sit chair consider always policy.	2004-08-23	\N
31	Christine Delgado	Packaging	Technician	86766739854	BS Food Science	Political tax technology point including leave. Ask political place. Free nice past event.\nMovie present practice radio. Weight young maybe agent he. After moment few.\nServe head decide vote.	2003-04-13	\N
32	Julie Cook	ESLP	Assistant	38285310498	BS Management	Culture force politics charge. Listen mission fact huge charge notice. Politics voice couple to eat.	1977-02-03	\N
33	Nicole Miller	Cooking	Technician	61189166625	BS Computer Science	Character sort follow. Democratic east leader treatment. Different response hot ok us tough.	1985-11-23	\N
34	Bradley Huber	TVP	Assistant	3782364307	BS Industrial Engineering	Tax approach course left order. Care happy forget choice.\nCharacter remain to nor worker. Despite above note color. Order range fast note past doctor especially.	1989-12-15	\N
35	Earl Berger	Coating	Technician	80480275175	BS Food Science	Single daughter real arm shake. Pull guess husband power teacher take.\nConsumer physical if cup child let. Right until suddenly visit. Carry most coach inside consider seven these.	1976-03-24	\N
36	Rachel Rose	Coating	Technician	78045658375	BS Economics	Onto reveal whose help watch bill red. Myself girl community analysis parent.\nBut happen practice company.	1988-08-04	\N
37	Summer Strickland	Hydration	Developer	741918208	BS Computer Science	Operation likely administration order. Stock piece enough during. Even player play receive again agreement.\nAmerican data study back behavior. Him investment economic.	1990-04-06	\N
38	Christine Lowe	Cooling	Developer	73452731561	BS Industrial Engineering	Strategy ball program land. That wall order cold. Budget piece company system smile five.	2004-04-07	\N
39	Jeffrey Simmons	ESLP	Developer	83290908925	BS Food Science	Night listen see visit town imagine. Foreign expert attorney rise American form.\nRecognize perhaps too sort true none later. Already while keep actually style.\nLead treat soon office.	2001-11-18	\N
40	Emily Wilson	ESLP	Engineer	77745253873	BS Food Science	Fill information letter eat. Move skin not technology save later article. Question we follow another positive call. Sound voice thing conference arrive hotel thought.	1981-06-09	\N
41	Thomas Lane	TVP	Staff	93447952695	BS Economics	Democrat financial company fine. Another eight deep various.\nHim campaign enjoy national as coach remember. Lead over agree sort old ground. Purpose whose know get own court tend employee.	2011-11-20	\N
42	Michael Montgomery	Cooling	Assistant	64437363595	BS Management	Interest seem next test skill significant kind.\nBehind house for painting partner protect what. Marriage lose also population guess station. Bad her short myself.	2018-11-03	\N
43	Christopher Woods	Cooking	Developer	61270813341	BS Economics	Year claim east student visit. Reveal player begin choose participant story himself. One Mrs war newspaper. Management walk here around alone.	2015-04-15	\N
44	Casey Dickerson	Cooling	Technician	19003776581	BS Food Science	Tv try under likely star. Here list into mother moment across gun. Wait enough painting probably example throw yet.	2008-12-02	\N
45	Maria Aguilar	Cooling	Assistant	68106614997	BS Management	Old practice stuff ability go perform really. Statement watch three. Popular close admit knowledge.	1999-03-19	\N
46	Krista Wright	Packaging	Engineer	49136602140	BS Computer Science	Suggest start race. Do role do race behavior cut main.\nTraining single benefit professional for natural tell analysis. Guess win this evidence.	2002-03-10	\N
47	Anita Nixon	Cooking	Staff	63259269890	BS Industrial Engineering	Feeling return pretty quickly. Position need same nor house.\nDo management hot on pressure. I board effort. Church benefit foot.	1982-02-03	\N
48	Joseph Williams	Hydration	Assistant	78808680427	BS Management	Least plant power she sometimes issue. Economic here east.\nRange focus source sign purpose remain people least. Natural else avoid smile rest dinner. Experience window nearly be offer herself.	2006-07-29	\N
49	Ronald Hendricks	Hydration	Assistant	75961767269	BS Industrial Engineering	Soldier responsibility range discover nice produce. Half heart where seven film low. Anything often his training.\nMajor ask ability individual operation. Large particularly manager.	2010-08-17	\N
50	Mrs. Tina Cline	ESLP	Assistant	38430293550	BS Economics	Seek no Congress campaign agree whether. Statement model mission account reduce. Fish institution way stage hear win green.	1990-12-20	\N
51	Nathan Johnson	Packaging	Engineer	51306121572	BS Food Science	Where piece party support. International list return work.	2011-12-15	\N
52	Amanda Gutierrez	ESLP	Assistant	66475679311	BS Computer Science	Factor claim far I long heart. Edge compare figure pass other. Question early election money current.\nPrepare position condition husband. White wear care.	2015-03-19	\N
53	Sean Mcgee	Coating	Engineer	12299871152	BS Food Science	Notice six rate notice. War section first enjoy civil structure whatever. Make seven until describe.\nIndeed spend action woman according as. Inside until peace yes PM drop commercial.	2020-10-04	\N
55	John Pancho	Packaging	Engineer	12345676543	BS Life Science	Good at Dynos	2023-01-10	\N
54	Bea Cruz	Cooking	Engineer	12345676542	BS Life Science	Great at cooking faux shrimp	2023-01-10	t
\.


--
-- Data for Name: emp_know; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.emp_know (emp_id, know_id, emp_know_delete_ind) FROM stdin;
13	35	\N
33	35	\N
36	37	\N
39	27	\N
17	27	\N
27	27	\N
44	35	\N
41	30	\N
36	27	\N
35	26	\N
10	30	\N
51	33	\N
4	30	\N
49	37	\N
13	28	\N
34	37	\N
42	36	\N
23	26	\N
31	29	\N
18	36	\N
10	36	\N
22	33	\N
23	30	\N
43	29	\N
29	34	\N
27	34	\N
49	34	\N
12	28	\N
5	45	\N
30	45	\N
31	46	\N
43	46	\N
37	46	\N
5	47	\N
37	47	\N
7	47	\N
48	39	\N
20	39	\N
5	41	\N
43	41	\N
5	42	\N
5	43	\N
33	48	\N
42	48	\N
\.


--
-- Data for Name: knowledge; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.knowledge (know_id, know_type, know_name, know_desc, prop_date, prop_by, app_status, know_delete_ind) FROM stdin;
26	Information	Improving hydration, cooking and cooling, and de-flavoring of plant-based proteins in the manufacture of meat substitutes	Dry beans, lentils and peas are a popular and growing choice in the diet of Americans. Factors driving the growth in consumption of pulses include widespread interest in ethnic foods and changes in Americans dietary awareness. As a group they are one of the most nutritionally-complete foods, inexpensive and widely available. High in protein, fiber and carbohydrates, and low in fat, these black beans, pinto beans, garbanzo beans, soybeans, lentils and peas have become a healthy and popular substitute for meat.\r\n\r\nExpanding Market for Meat Substitutes\r\nThe trend toward vegan, vegetarian and flexitarian diets is greatly influencing the use of plant-based proteins as meat and seafood substitutes. Market analysis prepared by The Good Food Institute (GFI) and the Plant Based Foods Association (PBFA), the trade association representing more than 160 plant-based food companies, reports that in 2019 the plant-based meat category alone was worth more than $939 million worldwide annually, with sales up18.4 percent compared to the prior year, and up 37.9 percent over the prior two years.  More than 208 million units of plant-based meat were sold in 2019.\r\n\r\nLeading this category are products such as Beyond Meat, which makes beef, sausage and beef crumbles under the brand Beyond, using primarily pea protein isolate. Impossible Foods produces the Impossible Burger, using soy protein concentrate, soy-protein isolate and potato protein. Soy and wheat-based proteins are also used in the Awesome Burger and Incredible Burger from Nestlé. Kraft Foods produces BOCA meatless patties using soy protein concentrate, isolated soy protein, and hydrolyzed soy protein as the main plant-based protein ingredients. And Good Catch Foods offers tuna substitutes using a blend of lentils, peas, chickpeas, soy and fava beans, like Naked in Water, that capture the taste and texture of real tuna.\r\n\r\nProcessing for Taste and Texture\r\nTo achieve the desired taste and texture for plant-based meat substitutes, manufacturers prepare pulses by subjecting them to processes such as hydration, cooking, de-flavoring, pasteurization and cooling. A wide range of product characteristics can be achieved by altering these process conditions. Supplemental ingredients and flavorings are added to arrive at proprietary blends. High-moisture extrusion and shear cell processes are used to define the texture and shape of the products, then molded into forms such as crumbles, strips, patties and sausages.\r\n\r\nThis article will focus on some of the latest processing technology related to hydration, cooking and cooling, de-flavoring and pouch cooling after pasteurization.\r\n\r\nContinuous Processing\r\nOver the past 40 years, continuous processing technology in the handling of pulses for cooking and cooling has evolved far beyond quality and throughput expectations of batch processes.  Processing labor hours have reduced to a fraction of what batch systems require.\r\n\r\nContinuous process systems slowly move pulses through an enclosed perforated drum resulting in the product being submerged in water, using an auger or screw to control dwell times. The pulses are hydrated, cooked and cooled to the same degree throughout their movement in the drum from entry to exit, ensuring uniform first-in/first-out (FI/FO) processing.\r\n\r\nThe conventional method of continuous process uses a rotary drum, where the enclosed auger/drum assembly rotates as one cylinder. A more recent continuous design has the auger rotating while residing within a stationary wedge-wire screen.  Each system has its advantages with processing pulses, depending on the need for gentle product handling, and changeover and cleaning requirements.\r\n\r\nAided by the integration of pre-programmed PLCs that ensure a precisely controlled process and recipe management, continuous-processing systems deliver precise automated control of hydration, cook and cool functions, resulting in uniform heating and cooling that achieves a totally consistent end product.\r\n\r\nThe most advanced of these continuous-process systems have the added benefit of providing an exceptionally low product damage rate of less than 1 percent.  Supporting this has been the development of two technologies that ensured more uniform processes, and allowed cookers and coolers to handle higher throughputs.\r\n\r\nThe first is a gentle mechanical stirring action on the pulses as they progress through the machine. The other is a system called Hydro-Flow, which applies water injection that puts the pulses in suspension, more evenly distributing the product loading across the width of the machine, and uniformly treating each particle.\r\n\r\nMuch of the technological developments integrated into continuous-process cookers and coolers, such as Hydro-Flow, were developed by Lyco Manufacturing, a leading manufacturer of commercial cooking and cooling systems for food processors.  These improvements have helped push the acceptance of continuous processing, where now, more than 50 percent of the dry bean market has adapted to continuous over batch systems.\r\n\r\nHydration\r\nHydration in pulse processing is necessary to prepare the pulse for subsequent cooking or extrusion, by increasing water weight from a dry state of approximately 12 percent moisture to as much as 58 percent moisture.\r\n\r\n"For hydration, continuous systems are much more effective than conveyor systems and static soak tanks of water," said Jeff Zittel, Vice President of Sales, Marketing, Applications Engineering and Service, with Lyco. "Hydration times are reduced from as much as from 4 to12 hours, to 1 hour or less, which is a huge improvement in productivity for processors of plant-based proteins."\r\n\r\nCooking and Cooling\r\nCooking and cooling plays a critical role in the processing of plant-based proteins for meat substitutes. They can be used to modify the outer texture of extruded soy products, as well as enabling the extruded pieces to be easily pulled into fibers resembling real meat. But for a growing number of processors of these meat substitutes the need for higher capacity lines with faster product change-overs has become a topline issue.\r\n\r\n“Food processors have become increasingly concerned about food safety, quick change-overs, and faster clean-up time and turn-around time,” said Zittel. “This trend is taking place around the globe to accommodate the needs of more diverse consumers, and particularly so with the manufacture of ready-to-eat meals, and cooking and cooling plant-based proteins for meat substitutes.”\r\n\r\nA recently-released continuous-processing system, called Clean-Flow, addresses this need, applicable to both cooking and cooling of pulses.\r\n\r\nThe Clean-Flow design begins with a very accurately made screw auger, similar to what is used in the systems mentioned prior. The auger resides in a stationary wedge-wire screen that encapsulates the screw from the 3:00 to 9:00 o’clock position. The tolerance between the screw and the screen is less than one-half a grain of rice.  Water agitation via Hydro-Flow is injected through the screen which keeps the pulse product off from the floor of the screen, where it is maintained in total suspension. The pulse runs through the cooking Clean-Flow system, then is immediately put through another Clean-Flow cooling system to stop the cooking process. Damage to fragile pulses amounts to a fraction of one percent.\r\n\r\n"A very unique aspect of this system is attributed to its namesake," added Zittel. "Clean-Flow is designed to reduce clean up from hours to minutes, because the screw is totally exposed for cleaning. During clean-up the wedge-wire screen is released from its fixed position, and is continually rotated 360 degrees around the screw alternately exposing the interior and exterior of the screen to clean-in-place (CIP) manifolds located in the cover of the machine. The screw can be rotated at the same time as the screen, again exposing all surfaces to the cleansing water sprays. The CIP can clean more than 98 percent of the machine without manual intervention." \r\n\r\nDe-flavoring\r\nDespite the growing interest in using plant-based pulse proteins as meat substitutes, their flavor often can limit their use. Eliminating undesirable aroma and flavor properties provides a greater opportunity for the inclusion of pulse proteins in foods.\r\n\r\nDe-flavoring removes the bitter taste from garbanzo beans, yellow split peas, lentils and other pulses. The process is optimally accomplished by steaming. One advanced continuous system that is particularly well suited for de-flavoring is the Vapor-Flow steam cooker.  The pulse is transported through the machine by an auger wrapped with a perforated screen. Steam is injected at the base of the cylinder at multiple points. The rotating auger ensures uniform heat penetration throughout the entire product load depth.\r\n\r\nAnother recently-released system, called Pressure-Flow, is a continuous cooker that is an ideal system for de-flavoring pulses. It reduces pulse cook times from 45 minutes down to 8 minutes or less. The system was specifically designed to hydrate, par-cook or fully-cook pulses, grains and other particulates. It provides plant-based protein processors with a unique continuous first-in/first-out pressure cooker, while offering the latest in fully-automated Clean-Flow technology in a pressure vessel.\r\n\r\nPouch Cooling after Pasteurization\r\n"Flexible packaging/pouches are a convenient, portable and environmentally-friendly method to package processed plant-based proteins, and particularly fully-processed meat substitutes, for food service and retail markets," explained Zittel. "Once product is processed and put into a package or pouch it can be pasteurized."\r\n\r\nAfter pasteurization, the pouched product needs to be cooled.  Water is the most economical and efficient medium for transferring or removing the heat. Cooling time depends upon the product, density, weight and recipe, and can vary from 20 to 120 minutes. USDA Regulations dictate that final product temperature must be close to 40°F or lower within a given period of time. It is important that pouches pass through the danger zone (130°F to 80°F) rapidly where bacteria are most likely to proliferate. Pouches may vary from a few ounces to more than 10 pounds, and in every case gradual cooling is important so as not to freeze the exterior while the core remains warm.\r\n\r\nCooling pouched plant-based proteins in the form of strips, burgers, sausages and crumbles is effectively achieved with a continuous system called Chill-Flow, which represents a state-of-the-art system for pouch cooling.\r\n\r\nThis system functions as a rotating drum with an attached auger, and a perforated skin sheet wrapped around it that is fixed to the auger flights so to eliminate pinch points.  These flights gently move the pouches through the system.  The pouches are carefully agitated with Hydro-Flow, turned over and massaged, while totally submersed in water that is 33 degrees F as they advance through the cylinder. Much more energy efficient than air cooling, water deluge belts or belt freezer methods. Once through the system – in a FI/FO sequence – the pouches, now at 40° F, are then gently deposited out of the system for subsequent packaging and storage in a freezer. Product damage is near zero percent.\r\n\r\nA Better Solution\r\n"Food manufacturers are approaching the processing of plant-based meat substitutes from many different perspectives – from the selection and blending of pulses, to the systems employed to achieve final products," added Zittel.\r\n\r\nBut the preparation of these dry beans, lentils, soy beans and peas for processing into plant-based meat substitutes is increasingly becoming standardized with the use of continuous-processing systems. These highly-automated systems maintain precise control over time, temperature and moisture, enabling higher throughput, a better ROI, and most importantly a more standardized and better quality product.\r\n\r\n	2022-05-15 00:00:00	Kevin Martin	Approved	\N
27	Information	Public Health Considerations	Farmed Meat\r\nConsumption of farmed meat, as well as fish and other “seafood,” and being in or near animal farming operations, pose several public health risk factors and consequences. Diets with high levels of animal product consumption have been linked to heart disease, type 2 diabetes, and colorectal cancer.  Red meat contains high levels of the amino acid derivative L-carnitine, with new research suggesting it plays a role in the production of metabolites associated with a higher risk for cardiovascular disease and inflammatory bowel disease. While regular consumption of seafood rich in omega-3 fatty acids is linked with health benefits such as reduced cardiovascular disease risk and improved cognitive development in human infants, there are not enough fish, both wild-caught and farmed, available for everyone globally to consume at recommended levels to capture these health benefits. \r\n\r\nMany pathogens that cause foodborne illness (Salmonella, E. coli, Campylobacter, and Listeria, for example) live in the guts of animals, and can then enter the food supply from animal manure runoff and irrigation water contamination, or through cross-contamination with meat if digestive tracts are severed during slaughter and processing. \r\n\r\nWorkers in farmed meat operations can be exposed to zoonotic pathogens and contend with bacterial infections; an estimated 25% of such workers in indoor operations suffer from a respiratory illness. \r\n\r\nPeople living near farmed meat facilities also face health risks from waterborne bacterial and chemical hazards from these operations, in addition to respiratory hazards and exposure to zoonotic pathogens.\r\n\r\nPlant-Based Meat\r\nPlant-based meats often have a comparable nutritional profile (calories, protein, and iron) to the meats they are designed to replace. They are food products that are typically primarily composed of wheat gluten, pea protein, or soy protein isolates, have undergone high levels of processing, often have high levels of sodium, and contain additives such as flavorings, colorings, and binding agents. The inclusion of coconut oil in some plant-based meats results in a saturated fat content similar to or higher than chicken or pig meat, but lower than that of cow meat. There is little evidence so far whether these ingredients and additives are beneficial or harmful to human health. \r\n\r\nIn contrast to plant-based meats, there is stronger evidence in the literature that less-processed soy foods such as tofu, tempeh, and soymilk, are associated with health benefits such as improved blood lipid levels, bone health, and reduced risks of type 2 diabetes and breast cancer. One plant-based meat additive that deserves further consideration though is heme iron, in the form of soy leghemoglobin, used specifically in products manufactured by Impossible Foods; since high levels of heme iron consumption from animal products is associated with increased risk for type 2 diabetes, cardiovascular disease, colorectal disease and cancer, and lung cancer, there may be a similar disease risk resulting from consumption of Impossible Foods products.\r\n\r\nThe chiefly known food safety concern of plant-based meats are allergens, as plant-based meat products commonly contain wheat and soy. Rarer allergic reactions can result from pea protein, lupin protein, and mycoprotein. Additives and gums in some plant-based meat products may also aggravate intolerances; carrageenan has the potential to cause gastrointestinal inflammation, alter intestinal microflora, and may be related to irritable bowel syndrome and colon cancer.\r\n\r\nThere is relatively little research on occupational exposure risks in plant-based meat manufacturing, but it is probably less hazardous compared to the risks faced by workers in farmed meat operations. There is concern about the exposure of workers in plant-based meat production to hexane, which is a solvent that can be used to process soy and pea protein isolates; hexane is neurotoxic and is a hazardous air pollutant. Little data exists on the magnitude of hexane usage in plant-based meat manufacturing, or on measures by plant-based meat manufacturing facilities to protect workers, prevent environmental releases, and monitor exposures to hexane.\r\n\r\nOf course, plant-based meat production relies heavily on crops, such as soy, wheat, and corn, which contribute to groundwater contamination due to nutrient runoff. The production of these crops often requires pesticide, herbicide, and fungicide application, which are associated with health problems for people working on and living near farms. The use of herbicides and fungicides also pose the potential for inducing resistance in pathogens and fungi to antibiotics and anti-fungal medicines, respectively. Still, a soy-based plant-based meat product requires far less soy production than a comparable farmed meat product that uses much more soy as an input for animal feed.\r\n\r\nCell-Based Meat\r\nSince cell-based meats are still in their development and prototyping stage, there is little information about their nutritional profiles and associated health consequences. It is still unclear if it is technically feasible to exactly replicate farmed meat in vitro. However, cell-based meat does present the opportunity of enhanced nutritional profiles compared to farmed meat, through fortification of the product with vitamins or omega-3 fatty acids.\r\n\r\nCell-based meat production could theoretically reduce the incidence of foodborne illness if produced in sterile environments, since animal carcass processing would not be involved. Fully sterile conditions are practically difficult to attain and antibiotics would probably still need to be applied to the tissue culture medium to suppress bacterial pathogens, though the antibiotic usage would likely be less intense compared to farmed meat operations.\r\n\r\nOccupational safety concerns related to cell-based meat are unclear due to the many unknowns of manufacturing processes and regulatory requirements surrounding cell-based meat production.\r\n\r\nFinally, it is unclear whether the antibiotic usage and waste management practices involved with cell-based meat production pose risks to people who work on or live near such production facilities.\r\n\r\n	2015-01-04 00:00:00	Brianna Pineda	Approved	\N
28	Information	Emerging Sources of Protein: Insect	4.2. Insect\r\nInsect consumption (entomophagy), whereby eggs, larvae, pupae and adults of certain insects are\r\nconsumed by humans, has occurred for thousands of years. Approximately 2000 species of insects\r\nhave been used as food [71] and they are part of the traditional diets of at least 2 billion people [72],\r\nparticularly in parts of Asia, Africa and South America where they provide important livelihood\r\nopportunities. Beetles are the most commonly consumed insects (31%), followed by caterpillars\r\n(18%); bees, wasps and ants (14%); grasshoppers, locusts and crickets (13%); cicadas, leafhoppers,\r\nplanthoppers, scale insects and true bugs (10%); termites (3%); dragonflies (3); flies (2%); and others\r\n(5%) [72]. However, more recently, insects have been identified as an alternative source of protein for\r\nthe Western world, not only as a delicacy or for emergency nutrition [73], supported by organizations\r\nsuch as the FAO [72] and the European Commission. Crickets, lesser mealworm and yellow mealworm\r\nare potential insects for application for food in the EU while black soldier fly, yellow mealworm and\r\nthe common housefly have potential for use in feed products [13].\r\nProponents of entomophagy argue that it has a lower environmental impact compared to meat\r\nproduction [74]. Significantly, they argue that insects do not compete for land, require less water and\r\nemit lower levels of greenhouse gases and NH3 than regular livestock. They can be reared on organic\r\nside-streams thus creating value from and reducing waste products. However, the environmental\r\nimpact of insect production is significantly influenced by insect’s diet, which in turn influences whether\r\nit can be used for food or feed purposes [75]. Another environmental advantage is that up to 80%\r\nof body weight is edible and digestible compared to 55% for chicken and 40% for cattle [35]. Being\r\ncold-blooded, they perform better in terms of feed conversion efficiency, and they reproduce more\r\nrapidly [76]. Many insects also have a favourable nutritional profile for humans, with most being\r\nhighly digestible (77–98%), high in protein (crude protein 40–75% on a dry weight basis) [10] and\r\na good source of essential amino acids, high in vitamins B1, B2 and B3 and the minerals iron and\r\nzinc [77]. However, many insects are deficient in certain amino acids, including tryptophan and lysine,\r\nand those with chitin exoskeletons have lower levels of digestibility. Insects vary considerably in fat,\r\nand thus energy levels, with some insects recorded as having 77 g/100 g dry weight. Some research\r\nFoods 2017, 6, 53 11 of 21\r\nargues that insects pose less risk of transmitting zoonotic diseases to humans, compared to animals\r\nand birds [72].\r\nMost insects are, however, still collected from their natural environment (usually forests), which\r\nrestricts supply according to season and location [78]. Furthermore, some researchers question\r\ninsect consumption from a food safety perspective, arguing that the safety of insects as food is\r\nunder-researched [77]. While insects are similar to other animal-derived products in that they are rich\r\nin nutrients and moisture (providing a medium for growth of unwanted microorganisms in certain\r\nconditions), the fact that insects are phylogenetically far removed from mammals, birds and some\r\naquatic species regularly consumed as food means that significant differences are expected when\r\nmaking comparisons between them in terms of risks [77]. Furthermore, many insects are consumed\r\nwhole, which includes their gut microflora which may affect microbiological quality of the food\r\nproduct [10] and specific health implications associated with using organic feedstocks to produce the\r\ninsects need to be assessed (for example (undesirable) substrate materials can be transferred into the\r\nprotein products and thus into the human food chain).\r\nNotwithstanding long traditions of domestication of bees and silk worms, and the practice of\r\nrearing insects for biological control, health and pollination [72] commercial insect farming for food\r\npurposes is only beginning to evolve, largely in proximity to concentrations of consumers. While\r\ninsects are an established part of food culture in some countries and are eaten out of choice, there is\r\nevidence of some reluctance by Western consumers to accept insects as food as they are often considered\r\nas pests, and a source of contamination, and thus to be avoided. Van Huis and colleagues [72] relate\r\nthe absence of a history of consuming insects to the difficulty of harvesting a proper meal of insects in\r\ntemperate zones (insects tend to be less abundant, smaller and found less often in clumps in temperate\r\nzones). Nonetheless, food products are available on the market including cricket protein bars produced\r\nby British company Next Step Foods, and are on the shelves in European supermarkets including the\r\nBelgian supermarkets Delhaize and Carrefour. Widespread adoption of insects for food purposes will\r\nnot however be achieved based on communicating their environmental and nutritional benefits. It\r\nwill be dependent on addressing what Rozin and Fallon [79] identify as three important motives that\r\nlead to product rejection: negative sensory properties (distaste), harmful consequences (perceived\r\ndanger) and “ideational” factors. Given that physical state is often used as a heuristic to evaluate\r\nfood, processing insect protein to render it into an unrecognizable (e.g., as an ingredient in a familiar\r\nproduct) could be a productive strategy. Similarly, ensuring insects and insect-based products are\r\nacceptable from a sensory perspective and are safe to eat will be critical.\r\nThe Belgian food safety authority allowed the sale of ten different types of insects for food\r\nconsumption in 2013 following a federal ruling. However, the EU novel food regulation does not\r\nyet allow insects for human consumption to be sold. Regulatory changes are expected but it is not\r\nclear when this will happen, which means companies are currently focusing on insects for animal\r\nfeed and pet food rather than human consumption. Commercial production of insects for human\r\nconsumption will require the establishment of new value chains. Given that they are most likely to be\r\naccepted as ingredients rather than whole, such a chain includes ensuring a safe and reliable feedstock\r\nfor the insect, mass rearing of insect larvae, their processing into insect ingredients, and application of\r\nthese ingredients in final food products. All of these activities need to be developed simultaneously,\r\nresulting in costs and risks. Some organizations and commercial companies are setting up production\r\non an industrial scale, e.g., the FAO established an insect farming project in the Philippines in 2010 [80],\r\nSwiss company Bühler is setting up pilot facility in China to process fly larvae and mealworms, and\r\nthere are a few industrial scale enterprises in various stages of start-up within Europe for raising insects\r\nsuch as black soldier flies. The establishment of a trade group called International Platform for Insects\r\nfor Food and Feed (IPIFF) is also significant. Nonetheless, current primary production systems remain\r\nexpensive, with a need to develop automation processes to make insect production economically\r\ncompetitive; extraction processing systems are also too costly and need further development [72].\r\n	2021-08-10 00:00:00	Tina Thomas	Approved	\N
29	Information	Current alternative protein market and consumption\r\n	Based on Mintel market analysis, there are an increasing \r\nnumber of consumers that are going to be \r\nvegetarian/vegan/flexitarian in the near future. The biggest\r\nmarket driver for alternative protein sources is increasing health \r\nconcerns among consumers, including sport enthusiasts and \r\nhealth addicts. The four biggest drivers of protein consumption \r\namong UK consumers listed by Mintel are muscle building, \r\nmuscle maintenance, weight loss, and weight maintenance,\r\naccounting for 33%, 36%, 42% and 47% respectively.\r\nThe demand for alternative protein sources is also seen to be on \r\nthe rise globally, with the total market size forecasted by Allied \r\nMarket research to reach £4bn by 2020. Europe accounts for \r\nalmost 40% of the overall market revenue, due to the increase \r\nin the consumption of high protein product (i.e. snacks and sport \r\nnutrition) from meat alternatives. 	2021-01-13 00:00:00	Andrew Hill	Approved	\N
30	Information	Downsides of Textured Vegetable Protein	What are the disadvantages of TVP?\r\nThe main disadvantages of including this product in your diet include:\r\n\r\nDifficulty digesting soy properly — When soy is not fermented (soaked and sprouted), it can be hard to break down due to antinutrients it contains, which block some of its minerals from being absorbed. This is one reason why fermented soy products are usually a better option, such as tempeh, miso or organic tofu.\r\nPossible allergenic reactions to soy — Soy is a common allergen and can cause side effects among some people, such as indigestion, rashes, hives and even serious complications, including anaphylaxis.\r\nLikely to be GMO — The vast majority of soy grown in the United States is genetically modified. Look for certified organic TVP if you do decide to purchase it.\r\nPotential affects on hormonal balance — Soy is a unique food because it’s high in compounds called isoflavones, which are a type of plant estrogen (or phytoestrogen). Phytoestrogens have the ability to act like human estrogen in the body, which sometimes has an effect on hormones if you eat lots of soy products on a regular basis.\r\nPossibility of consuming other harmful ingredients — Because TVP is found in mostly processed foods, you’re likely to consume additives, preservatives, lots of sodium and added sugar, and other unwanted ingredients if you consume a lot of products that contain it. Plus, there’s a small risk of consuming solvents that are left lingering in TVP due to the manufacturing process.	2022-02-03 00:00:00	Cassandra Moore	Approved	\N
31	Information	PDCAAS	PDCAAS is a method of evaluating the quality of a protein and was adopted by US FDA & FAO/WHO in 1993.\r\n\r\nThe equation is as follows: Protein Digestibility-Corrected Amino Acid Score\r\n\r\nIn the U.S., PDCAAS can be important for food labeling. When a protein claim is made, PDCAAS is used to calculate the %DV on the Nutrition \r\nFacts panel. Protein complementation can be used to enhance %DV within a product. \r\n(%DV = percent daily value = protein grams/ daily requirement, protein grams = protein per serving * PDCAAS)\r\nPDCAAS is often used to calculate (and optimize for) protein quality via food combination based on the debunked idea of protein \r\ncomplementation. Amino Acid Score is of low importance (except for severely restricted diets), as the body can store amino acids across \r\nmealtimes. Also, Protein Digestibility is typically high (>0.75). \r\nPDCAAS doesn’t consider antinutritional factors (e.g., trypsin inhibitors) and non-absorptive losses (e.g., large intestine microflora). In 2013, \r\nFAO proposed changing to DIAAS (Digestible Indispensable Amino Acid Score) which measures digestibility at the end of the small intestine.\r\nProtein Digestibility is typically measured using rats, although an in vitro assay is now available from Megazymes. 	2020-10-21 00:00:00	Brittany Bass	Approved	\N
32	Information	What are methods of texturizing proteins?	Method Example\r\nCoarse aggregate gelation Tofu\r\nFine network gelation JUST Egg\r\nHydrocolloid gelation Plant based yogurts\r\nLow moisture extrusion TVP\r\nHigh moisture extrusion Gardein\r\nShear cell Wageningen\r\nFiber spinning Ford, General Foods, Bac’O’s\r\nElectrospinning Cultured meat scaffolds, Unilever WO2012084427A1 \r\nFreeze texturization of a gel Freeze-thaw tofu\r\nDeep-fry texturization Tofu puffs\r\nDry heat Tofu crumbles, baked tofu\r\nSkin formation on boiling Tofupi –> vegetarian duck\r\nFibers in a protein gel Guelph\r\nDough formation Seitan\r\nMycelia Quorn, tempeh\r\n3D printing Redefine Meat\r\n	2016-12-23 00:00:00	James Bailey	Approved	\N
33	Information	Increasing Acceptance	Our previous review included some studies which showed that additional information about\r\ncultured meat could influence consumers’ views, and that less technical explanations and higher\r\nperceived market share were associated with increased acceptance [12,39,40,69]. This section will\r\ndiscuss experimental studies which demonstrated an effect on acceptance of certain interventions.\r\nSeveral recent studies have demonstrated that cultured meat acceptance can be increased by\r\nproviding additional positive information. Zhang, Li and Bai [33] found that providing additional\r\ninformation about the environmental benefits of cultured meat increased acceptance amongst urban\r\nChinese consumers. Mancini and Antonioli [18] found that providing additional positive information\r\nabout cultured meat significantly increased the various measures of acceptance including the willingness\r\nto buy, but not the willingness to try.\r\nRolland et al. [19] found that additional information about the various benefits of cultured\r\nmeat significantly increased acceptance, and tasting what participants thought to be cultured meat\r\nsignificantly increased acceptance further. The authors tested three types of information (societal\r\nbenefits, personal benefits, and meat quality and taste). They found that, while all three led to significant\r\nincreases in acceptance, information about the personal benefits led to a significantly greater increase\r\nthan the other information conditions. This provides evidence that messages aiming to persuade\r\nconsumers to adopt cultured meat should focus primarily on the benefits to the consumer (rather than\r\nthe benefits to society, the environment, or animals). Verbeke et al. [53] noted that the latter tend to be\r\nmore obvious to participants to begin with.\r\nNomenclature and terminology are also important. Bryant and Barnett [14] found that different\r\nnames had a significant effect on the measures of acceptance. We found that “clean meat” led to a\r\nsignificantly higher acceptance than “lab grown meat”, with “cultured meat” and “animal-free meat”\r\nscoring somewhere in between. Further, we showed that the difference between groups was accounted\r\nfor by the positivity of associations participants gave. This indicates that the mechanism by which\r\nnomenclature affects acceptance is by anchoring to concepts which are more or less appealing in the\r\ncontext. Similarly, Geipel et al. [16] found that German participants reading about cultured meat in\r\ntheir non-native English (vs. their native German) experienced less disgust, and subsequently had a\r\nhigher willingness to eat it. The authors note that this foreign language effect has been observed in\r\nother contexts, appearing to make people behave in a more utilitarian manner [70].\r\n	2021-03-11 00:00:00	Robert Alvarez	Approved	\N
34	Information	Protein Demand	In addition to increased demand arising from population growth, increased demand for protein\r\nglobally is driven by socio-economic changes such as rising incomes, increased urbanisation, and aging\r\npopulations whereby the contribution of protein to healthy aging is increasingly recognised [5,6], and\r\nrecognition of the role of protein in a healthy diet. Economic development and increased urbanization\r\nis leading to major transitions in population-level dietary patterns in low and middle income countries\r\nin particular, such that most of the global increases in demand for foods of animal origin are seen\r\nin developing countries [6]. Some forces, however, provide a countervailing force slowing demand\r\nin developed countries. Such factors include increased awareness of the impact of food production\r\nand consumption on the environment and on health. In the context of protein, the negative impact is\r\nmainly associated with animal-derived protein with reports that 12% of GHG emissions derive from\r\nlivestock production and that 30% of human-induced terrestrial biodiversity loss can be attributed to\r\nanimal production [2]. Land use is also a concern; for example, in the EU two thirds of total agricultural\r\narea is used for livestock production and around 75% of protein-rich animal feed is imported from\r\nSouth America using large tracts of land there also [2]. Health concerns arise with over-consumption of\r\nprotein, particularly when linked with saturated fatty acids and over consumption of processed meats.\r\nEthical issues about animal production could also stifle demand with a trend towards flexitarianism\r\nand initiatives aimed at reducing meat consumption evident in some markets	2020-11-16 00:00:00	Kaitlin Roth	Approved	\N
35	Information	Regulatory Framework	PBMs are regulated in a similar manner as other non-animal foods. In the United States, the Food and Drug Administration (FDA), and specifically the Center for Food Safety and Applied Nutrition (CFSAN), oversees food inspection, labeling, packaging, imports, and facility safety. Most PBM products contain simple ingredients that have previously been approved for human consumption. Novel ingredients may be subject to additional evaluation processes. For example, soy leghemoglobin, produced via genetic engineering, filed for “generally recognized as safe” status with the FDA for use as a color additive17. In the European Union (EU), current policy and regulation are supportive for alternative proteins innovation and investment. In 2018, the European Commission presented a “EU Protein Plan”, which encourages the production of alternative proteins for human consumption, and listed existing EU policy instruments that “provide options for strengthening the development of EU-grown plant proteins”. Many novel PBM products are classified under the Novel Food Regulation which regulates “food that had not been consumed or do not exist in the EU before 15 May 1997”23. Australia, Canada, and New Zealand have also introduced legislation to guide oversight of novel foods13. Government oversight is also required for food labeling. In 2018, The United States Cattlemen’s Association petitioned the Food Safety and Inspection Service (FSIS) “to exclude products not derived directly from animals raised and slaughtered from the definition of “beef” and “meat”29. The use of terms such as steak, sausage, bacon, fillet, etc. for PBMs is subject to scrutiny and restriction in many EU member states as well.\r\n\r\n	2015-11-16 00:00:00	Jessica Norman	Approved	\N
36	News	Spanish Food Tech Keeps Growing in 2022	Madrid, December 21st — Eatable Adventures, one of the worlds leading agri-food accelerators, has presented the data from its annual study "The State of Foodtech in Spain 2022," a report gathering key information on the characterization and investment evolution of the Spanish food-tech entrepreneurial ecosystem.\r\n\r\nBroadly, 2022 has been a positive year for the sector in the country. Despite the macroeconomic context, the Spanish startups have been supported by investors, companies and governments, which have taken a much more active role in the growth of the Spanish ecosystem.\r\n\r\nIn 2022, Spain remains in the global top 10 ranking in terms of number of food-tech startups, whose latest census, according to the report, totals 412 startups. As for the key areas of the food-tech sector, once again this year, 4 major categories were identified, showing a fairly balance among them: Agritech (24%); Food Production and Transformation (34%); Logistics, Distribution and Retail (25%); and Restaurant Tech (16%).\r\n\r\nSpanish startups are solvent at a technological level and have a solid level of development. The percentage of startups that decide to patent their solutions or generate utility models is growing: 32,9% of startups have patents, 56,6% have a trademark registration and 29% have a trade secret. There is significant growth in the use of artificial intelligence, with an increase of more than 12 points, compared to last year, as well as in machine learning and IoT, with an increase of 8,5 and 9,6 points, respectively. Regarding the degree of technological development (TRL) of the startups, more than 80% have market-ready solutions and 14% are still at an intermediate stage.\r\n\r\nThis year, the total investment figure stands at 268 million euros, an increase of 9,38% compared to the previous year, not considering the investment round achieved by Glovo (450 million euros). In addition, the increase in Series A rounds stands out, growing by nearly 20%, 5 points more than in 2021.	2017-10-02 00:00:00	Elizabeth Martinez	Approved	\N
37	Information	This is Not Related to Alternative Protein	Public base short. Admit would administration possible machine. Chance consumer boy address main who ask. Treatment attention push middle animal station as.	2017-03-19 00:00:00	Jeffrey Wilson	Rejected	\N
38	Information	This is Not AP	Lorem Ipsum Lorem Ispum	2016-11-10 00:00:00	Sandra Washington	Rejected	\N
45	News Article	Article about Batman	Fake Batman Misinformation	2023-01-08 20:34:04.693286	John Doe	Waiting	\N
40	Tutorial	How to play Guitar	First step is to....\n\nThen you need to...\n\nAfter that...	2023-01-08 20:11:19.752591	Jessica Smith	Approved	\N
44	News Article	News about Superman X	This is news about superman X	2023-01-08 20:32:43.988557	John Doe	Approved	\N
47	Tutorial	How to Train Your Dragon	Dragons	2023-01-09 22:03:04.895151	Mikhail Franco Planas	Approved	\N
46	Research	Research on Food Cooking 101	Step 1:\nStep 2:\nStep 3:\n\nThat is how you cook!	2023-01-08 20:50:37.034954	Juan Dela Cruz	Approved	\N
39	Tutorial	This Article is for Approval	This article is about Alternative Protein but is still waiting for approval	2020-06-12 00:00:00	Mary Davidson	Approved	\N
41	Tutorial	How to play Guitar	First step is to....\n\nThen you need to...\n\nAfter that...	2023-01-08 20:11:19.786876	Jessica Smith	Approved	\N
42	News Article	Spiderman	This is a news article about spiderman	2023-01-08 20:15:04.052946	John Doe	Approved	t
43	General	General Article	What	2023-01-08 20:28:51.977589	Mikhail Franco Planas	Rejected	t
48	News Article	Mooki Recent Investments	Mooki X\nMooki Y\n\nThe word investment.	2023-01-10 00:29:37.895963	Bea Cruz	Waiting	\N
\.


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team (team_name, team_desc) FROM stdin;
TVP	In charge of receiving Textured Vegetable Protein
Hydration	In charge of combining heated water, broth, and or/fats to TVP
ESLP	Stands for Extended Shelf-Life Processes. In charge of prolonging             shelf life
Cooking	In charge of using various thermal process such as frying and             boiling
Coating	In charge of adding adhesive components and desered exterior             coatings
Cooling	In charge of refrigeration, freezing, or a combination of these             methods
Packaging	In charge of storing and packaging based on requirements and             customer uses
\.


--
-- Name: emp_emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emp_emp_id_seq', 55, true);


--
-- Name: emp_know_emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emp_know_emp_id_seq', 1, false);


--
-- Name: emp_know_know_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emp_know_know_id_seq', 1, false);


--
-- Name: knowledge_know_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.knowledge_know_id_seq', 48, true);


--
-- Name: emp emp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp
    ADD CONSTRAINT emp_pkey PRIMARY KEY (emp_id);


--
-- Name: knowledge knowledge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.knowledge
    ADD CONSTRAINT knowledge_pkey PRIMARY KEY (know_id);


--
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (team_name);


--
-- Name: emp_know emp_know_emp_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp_know
    ADD CONSTRAINT emp_know_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.emp(emp_id);


--
-- Name: emp_know emp_know_know_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp_know
    ADD CONSTRAINT emp_know_know_id_fkey FOREIGN KEY (know_id) REFERENCES public.knowledge(know_id);


--
-- Name: emp emp_team_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emp
    ADD CONSTRAINT emp_team_name_fkey FOREIGN KEY (team_name) REFERENCES public.team(team_name);


--
-- PostgreSQL database dump complete
--

