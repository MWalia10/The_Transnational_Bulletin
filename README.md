# The_Transnational_Bulletin

The Transnational Bulletin endeavours to serve as one of the most holistic spots for global news. It offers news from the following nations in their native as well as English language:

- Saudi Arabia (Arabic)
- France (French)
- India (Hindi)
- Russia (Russian)
- Argentina (Spanish)

The system's working can be better explained by decomposing into the following major sub-tasks

#### - Data Collection: 
The data has been collected using Google News APIs available for different languages. The system makes API calls and retrieve the news headlines, links and brief descriptions in native language. The data, retrieved in the form of json file is pre-processed and further used.

#### - Language Translation: 
Since the Google News API sends news in native languages, MBart50 Seq2Seq translation model has been employed form Hugging Face's transformer library that translates the news and it's description to English language so as to cater a wider audience.

#### - User Interface and Integration: 
After having performed the preliminary steps, the system has all the data to be presented ready. For the sake of better user experience, the information is displayed on a frontend developed using HTML, CSS and JavaScript and the entire system comes together using Flask as a Backend language. 

In its present state, the system is static in nature due to the computation constraints one faced owing to the lack of resources. However, it can be developed further so that the API is called periodically and the news is therefore updated frequently. 



For any other suggestions or potential opportunities, please free to contact:

Muskaan Walia (mwalia_be19@thapar.edu)

Suvrat Arora (sarora1_be19@thapar.edu)
