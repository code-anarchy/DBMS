from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json


# MongoDB connection string
uri = "mongodb+srv://codesrisha:Zygf4fUYScWteOWk@cluster0.my38l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["abdsa"]

collection = db["your_collection_name"]  # Replace with your collection name

# Case data
case_data = {
    "case_id": "2024 INSC 676",
    "dairy_number": "4177 of 2024",
    "judges": [
        "Sudhanshu Dhulia",
        "Pankaj Mithal"
    ],
    "parties": {
        "appellant": "SK. Golam Lalchand",
        "respondent": "Nandu Lal Shaw @ Nand Lal Keshri @ Nandu Lal Bayes & Ors."
    },
    "jurisdiction": "Supreme Court of India",
    "case_type": "Civil Appeal",
    "judgment_date": "September 10, 2024",
    "judgment_details": {
        "paragraphs": [
            {
                "number": 1,
                "text": "Heard Shri Rauf Rahim, learned senior counsel for the appellant and Shri Pijush K. Roy, learned senior counsel for the respondent No. 1."
            },
            {
                "number": 2,
                "text": "The dispute in this Civil Appeal is about the property measuring more or less 6 Cottahs 1 Chittack and 30 sq. ft. along with 17 rooms (about 4395 sq. ft. which comprises of tile sheds/huts) situate at 100/3 Carry Road, Howrah."
            },
            {
                "number": 3,
                "text": "The plaintiff-respondent Nandu Lal claims that he had acquired rights in the aforesaid property through his father late Salik Ram along with his other brothers and that Brij Mohan, his cousin, the son of his uncle late Sita Ram, had no exclusive right to sell the property in favour of anyone much less to one of the tenants S.K. Golam Lalchand, the defendant-appellant."
            },
            {
                "number": 4,
                "text": "The Title Suit No.212/2006 filed by the plaintiff-respondent Nandu Lal was dismissed by the court of first instance as he failed to prove his possession but in appeal the decree was reversed and the suit was decreed disbelieving the family settlement and holding that there was no partition of the property. The judgment and order of the First Appellate Court was affirmed by the High Court in Second Appeal."
            },
            {
                "number": 5,
                "text": "Aggrieved by the judgment and order of the First Appellate Court and its affirmation by the High Court vide judgment and order dated 06.07.2021, the defendant-appellant has preferred this appeal."
            },
            {
                "number": 6,
                "text": "The facts in brief are that the suit property was admittedly purchased by the two brothers namely, late Sita Ram and late Salik Ram in 1959 from one Sahdori Dasi and both of them had equal rights in the said property."
            },
            {
                "number": 7,
                "text": "It is alleged that one of the brothers late Salik Ram gifted his share in the suit property to his brother late Sita Ram who allegedly became the absolute owner of the entire property. The aforesaid late Sita Ram died intestate in 1975 leaving behind his son Brij Mohan and three daughters who appear to have relinquished their rights in the suit property in favour of their brother Brij Mohan. It is also alleged that the suit property under the family settlement was settled in favour of Brij Mohan."
            },
            {
                "number": 8,
                "text": "On the other hand, plaintiff-respondent Nandu Lal alleges that his father late Salik Ram made no gift of his share in the suit property in favour of late Sita Ram and that there is no family settlement as alleged by the other side. Therefore, Brij Mohan, the son of late Sita Ram, had no right to transfer the whole of the property in favour of one of the tenants, defendant-appellant S.K. Golam Lalchand and the sale deed in this regard dated 19.05.2006 is void."
            },
            {
                "number": 9,
                "text": "Upon the aforesaid sale of the entire suit property by Brij Mohan to defendant-appellant S.K. Golam Lalchand, the plaintiff-respondent Nandu Lal filed Title Suit No.212/2006 for declaration and permanent injunction claiming that the defendant-appellant S.K. Golam Lalchand could not have acquired any right, title and interest in the suit property by virtue of any sale deed, if any, executed by Brij Mohan and that he has no right to dispossess other tenants from the suit property and, therefore, he, his men and agents be restrained from taking forcible possession of any tenanted portion and from causing any disturbance in the possession of the plaintiff-respondent Nandu Lal."
            },
            {
                "number": 10,
                "text": "The plaintiff-respondent Nandu Lal alleged that the suit property was admittedly the joint property of both late Sita Ram and late Salik Ram. Late Salik Ram never made any gift of his share in the suit property in favour of late Sita Ram. There was no family settlement settling the suit property in favour of Brij Mohan, son of late Sita Ram. Since the property has not been partitioned, Brij Mohan could not have sold the same in entirety."
            },
            {
                "number": 11,
                "text": "The suit was contested by the defendant-appellant S.K. Golam Lalchand as well as Brij Mohan on the allegation that late Salik Ram, sometime in 1960, gifted his share in the suit property to late Sita Ram. Thus, late Sita Ram became the absolute owner. Upon his death in 1975, the property devolved upon his son Brij Mohan and three daughters who relinquished their rights in favour of Brij Mohan, thus, making Brij Mohan the absolute owner of the entire property. The defendant-appellant S.K. Golam Lalchand by filing a separate written statement stated that he is a bona fide purchaser in good faith of the whole property vide registered sale deed dated 19.05.2006 executed by Brij Mohan. The said sale deed, in unequivocal terms, states the manner in which Brij Mohan had acquired the property. Therefore, the suit of the plaintiff-respondent Nandu Lal is misconceived and liable to be dismissed."
            },
            {
                "number": 12,
                "text": "On the pleadings and submissions of the parties, the moot question which has arisen before us in the appeal is whether Brij Mohan, son of late Sita Ram, alone was competent to transfer the entire suit property by way of sale deed dated 19.05.2006 in favour of defendant-appellant S.K. Golam Lalchand."
            },
            {
                "number": 13,
                "text": "The plaintiff-respondent Nandu Lal, in order to substantiate his case, apart from other documents and oral evidence, brought on record the original deed of purchase of the property of the year 1959 Exh.1 and he himself appeared as a witness PW-1 to prove his case. The said original sale deed is undoubtedly in the joint name of late Salik Ram and late Sita Ram, both of whom acquired equal rights in the purchased property. This position is otherwise also admitted to the parties."
            },
            {
                "number": 14,
                "text": "The defendant-appellant S.K. Golam Lalchand or Brij Mohan has not led any evidence to prove the gifting of the share by late Salik Ram in favour of late Sita Ram. No gift deed in this regard has been produced in evidence. Therefore, as a natural consequence, both the brothers late Salik Ram and late Sita Ram continued to be the joint owners of the property."
            },
            {
                "number": 15,
                "text": "On the death of Sita Ram, his share in the suit property naturally devolved upon his son Brij Mohan and three daughters. No evidence was brought on record to establish that the daughters have relinquished/gifted their rights in the suit property in favour of their brother Brij Mohan. In this way, Brij Mohan had not acquired the rights in the property possessed by his sisters."
            },
            {
                "number": 16,
                "text": "Even the claim of the defendant-appellant S.K. Golam Lalchand or Brij Mohan to the suit property on the basis of the family settlement has not been proved. The settlement has not been adduced in evidence. Therefore, by no stretch of imagination, it can be said that Brij Mohan had acquired exclusive right in the entire property acquired and possessed by late Salik Ram and late Sita Ram by virtue of the sale deed 1959 Exh.1."
            },
            {
                "number": 17,
                "text": "Therefore, Brij Mohan had no exclusive right in the property to sell the same in entirety in favour of defendant-appellant S.K. Golam Lalchand."
            },
            {
                "number": 18,
                "text": "There being no valid transfer of the property by Brij Mohan in favour of defendant-appellant S.K. Golam Lalchand, the High Court was right in affirming the decree passed by the First Appellate Court and declaring that the suit property is still owned by plaintiff-respondent Nandu Lal and that there had been no valid transfer of the property by the defendant-appellant S.K. Golam Lalchand."
            },
            {
                "number": 19,
                "text": "In our considered opinion, the decree of the First Appellate Court as affirmed by the High Court is unassailable and the appeal is liable to be dismissed."
            }
        ]
    }
}

# Insert the case data into the MongoDB collection
result = collection.insert_one(case_data)

# Output the inserted ID
print("Case data inserted with ID:", result.inserted_id)
