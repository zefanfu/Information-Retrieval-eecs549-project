#This is the project for Information Retrieval course

Preparing for a perfect trip and geting all the information easily of a dream destination is always a problem for travel enthusiasts. In the real world, when travelers are planning for a trip, they need to go to diﬀerent websites to gather information. Therefore, we want to build a search engine that could provide a one-stop service that can provide many information that a traveler wants to know.

In order to build such a search engine, we formulate the problem into an information retrieval model. Firstly, we selected several open datasets that meet our needs, which include the Yelp open dataset that have restaurant and shop information, the countryside vegetarian restaurant information, and the countryside museum, zoo information. Each of the dataset has over 30,000 records. We also embedded some APIs such as weather info, local time, and Google Map into our website in order to enrich our system. Secondly, we made some pre-process to the raw dataset we fetched online and stored them into MySQL database. Finally, we used the document ranking knowledge we learned in class such as TF-IDF and cosine similarity to rank our retrieved documents. We also did some research on IR document ranking and used some
other methods such as Kendall’s Tau to further adjust and improve our ranking results. Besides, we made some process on the query such as stemming, stopword removing, word spell checking before doing the document retrieval in order to make our system more user friendly.

Please see eecs 549 final report.pdf for more detailed information
