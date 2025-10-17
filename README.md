# README

## Before you begin

Do NOT fork this project in GitHub, this will make your solution visible to other candidates and will be considered an automatic failure! Instead clone it to your local machine and push it up to your own personal github without directly linking to this repo. When you are done send the link to your repo to your point of contact.

## Setup

For development environment setup, project commands, and usage instructions, please see [HELP.md](HELP.md).

## The test

### Description Of Problem

At Elixir we often have to work with third party apis and ingest data into our system, we write bespoke programs that we call `biz_rules` to perform this integration. This test is a scale model of the sort of work we do quite frequently and is quite reflective of what a typical day might look like, the system uses [django rest framework](https://www.django-rest-framework.org/) to create a viewable api in the browser.

It is designed as a way to learn the mechanics of iTraX, if you are successful in your application, you will be working on a system similar to this (but on a much larger scale).

We have selected some api services and you may choose whichever one you like (please do choose ONLY one) and write the code in the `core/biz_rule.py` file (please see the `Services` section below for details).

Your task can be broken down into three parts:

* Study the api docs of the _one_ service you have chosen.
* Write a biz_rule that consumes data from one of the api end points.
* Ingests that into our test system using the provided models.

To be clear; you will not need to write your own models, or edit existing models, nor are you expected to consume all the data the end point returns, some of these end points contain hundreds of megabytes of data, you can ingest as much data as you want to, but you do not have to consume everything.

### The Services

- [Pokemon](https://pokemontcg.io/)
- [Magic: The Gathering](https://scryfall.com/docs/api)
- [Marvel](https://developer.marvel.com/)
- [Open Trivia](https://opentdb.com)
- [Cocktail DB](https://www.thecocktaildb.com/)


### Running your biz_rule

Running your integration (ingesting the data into the system) is as simple as `just bizrule` (assuming you are inside a devbox shell).
