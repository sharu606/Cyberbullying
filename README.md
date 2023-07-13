# Cyberbullying detection

## Problem Statement
Hateful comments can affect people’s physical and mental health. We have come across this in our day-to-day life, and the solution we have come up with is to detect such comments and take action against them. We are using a Machine Learning algorithm to detect hateful comments and their severity to take action depending on it. The aim of this project is to accurately identify and flag these hate speech or hateful comments on Instagram (Social Media). The project aims to improve user experience by reducing the spread and impact of hate speech, which can be harmful, offensive, and divisive.

## Description
* The algorithm has 2 phases.
1) During the initial phase, the primary objective is to identify and detect comments that exhibit hateful content. Following this identification process, the identified hateful comments undergo a filtering mechanism, subsequently serving as input for the subsequent phase.
2) The second phase involves classifying the hateful comments based on their severity into 2 levels
   a) High-severity hateful comments
   b) Low-severity hateful comments
* Actions are taken based on their severity.
  - High-severity hateful comments are automatically removed from display.
  - Low-severity hateful comments are tagged as "Hate" and users are given a choice to either remove them from view or view them.
 
## Modules
<img src="https://github.com/sharu606/Cyberbullying/blob/0849c39db867535f0997b5985fe7069a8ab8269a/Untitled%20(4).png" height="500"/>

**1) Dataprovider module**
- The dataset with hateful comments to train the algorithm is collected online. 
- There are over 20,000 comments provided with the classification of hateful or non-hateful comments.
- The hateful comments from the dataset are filtered and are then classified into high-severe and low-severe hateful comments.
  
**2. Preprocessing module**
-  Pre-processing refers to the transformations applied to the data before feeding it to the algorithm. 
- This Pre-processing includes of 
   - Rescaling of data, 
   - Tokenization of the data,
   - Stemming of the data, and
   - Removal of punctuations and numbers.

**3. Feature extraction module**
- We are using the TF-IDF algorithm for feature extraction from natural language comments. 
- TF-IDF algorithm short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.

**4. Classification module**
- Random forest classifier is an ensemble learning algorithm that combines multiple decision trees to make predictions. It is used for classification tasks, where the goal is to assign class labels to input data.
- The algorithm creates a collection of decision trees, each trained on a random subset of the training data. This process is called bootstrapping.

## Tech Stack
* __Front-end__
    - Android Studio/Visual Studio Code
    - React JS
    - Flask
* __Back-end__
  - Python
## Screenshot
### Screenshot of the warning to the user
<img src="https://github.com/sharu606/Cyberbullying/blob/b57b12eda94334cdd06c91383a08afdecd4b3336/images/Screenshot%20(586).png" height="400"/>

### If the user selects "Yes", all the Low-severity hateful comments are removed from view.
<img src="https://github.com/sharu606/Cyberbullying/blob/b57b12eda94334cdd06c91383a08afdecd4b3336/images/Screenshot%20(590).png" height="400"/>

### If the user selects "No", all the Low-severity hateful comments are displayed with a "Hate" tag.
<img src="https://github.com/sharu606/Cyberbullying/blob/b57b12eda94334cdd06c91383a08afdecd4b3336/images/Screenshot%20(584).png" height="400"/>

## Working video
[Demo Link](https://youtu.be/F5WklhB1WcM)
  
