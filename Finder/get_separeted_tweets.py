#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

#http://www.tweepy.org/ biblioteca usada
import tweepy

#credenciais de acesso
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_key = "access_key"
access_secret = "access_secret"

#method to get a user's last tweets
def get_tweets(username):
	print('Tweeter sendo baixado:',username)

	#buffer dos tweets
	tweets_for_csv = []
	#auth e criação do cliente
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#numero de tweets maximos por usuario do tweeter
	number_of_tweets = 5000

	#header do dataset
	if(len(tweets_for_csv) == 0):
		tweets_for_csv.append(['Pessoa','Data', 'Texto', 'Retweets', 'Likes'])

	#adiciona info de um tweet ao buffer global
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
		tweets_for_csv.append([username, tweet.created_at, tweet.text, tweet.retweet_count, tweet.favorite_count])

		#arquivo de saida
	outfile = "./Output/{0}.csv".format(username)
	with open(outfile, 'w', encoding='utf-16') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


#func de entrada
if __name__ == '__main__':
	#extrai os nomes das pessoas do arquivo txt
	vips = []
	filepath = './ToDo.txt'  
	with open(filepath) as fp:  
		line = fp.readline()
		while line:
			nome = line.strip().replace(" ", "")
			if(len(nome) > 0):
				vips.append(nome)
			line = fp.readline()

	#para cada pessoa que achou busca os tweets dele
	for name in vips:
		get_tweets(name)


