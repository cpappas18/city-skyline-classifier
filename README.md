# City Skyline Classifier 
This repository showcases a Convolutional Neural Network that classifies images of the Toronto, New York, and Paris skylines using their famous landmarks. Particularly, the network was trained using images of the CN Tower, the Empire State Building, and the Eiffel Tower, from both up-close and distant viewpoints.

My image dataset was scraped from Bing Images using the keywords specified in the 'bing-image-scraper.py' file. I used roughly 800 training images, 200 validation images, and 250 testing images for each city. The training accuracy is approximately ~0.9983 while the validation and testing accuracies are about ~0.7900. Evidently, the model has overfitted to the training data and is stuck at a local minimum in its error function. It is clear that I was limited by the size of my training dataset, and to improve performance and reduce overfitting I would need a much larger set of images. 

Regardless of its accuracy, this project was a really fun challenge for me. Although the code for this CNN is very similar to my last project, I delved a bit deeper into the research on this topic to get a better understanding of the right number of hidden layers, their nodes, and different activation functions. It was exciting to discover that it's quite easy to scrape a dataset off of a search engine, meaning I don't have to be limited by existing datasets but instead I can be creative with my classification. 
