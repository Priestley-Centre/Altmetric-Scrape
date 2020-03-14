# Altmetric-Scrape
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Priestley-Centre/Altmetric-Scrape?include_prereleases)](https://github.com/Priestley-Centre/Altmetric-Scrape/releases/tag/v1.0)
[![GitHub](https://img.shields.io/github/license/Priestley-Centre/Altmetric-Scrape)](https://github.com/Priestley-Centre/Altmetric-Scrape/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Here's the story. I was about to submit an article to an IOP journal. It referred quite a lot to another paper published in the same journal, which had already been talked about on twitter. I needed a way to contact all the tweeps that talked about it before, to let them know that the paper cast a new light on what they had shared.

This (very simple) python script consists of a single function which checks the [altmetric](https://www.altmetric.com/) page for a paper and returns all the twitter handles as a de-duplicated list.

for example:

    scrape("https://iop.altmetric.com/details/5152221/")

returns a list

    ['@handle0', '@handle1', '@handle2', '@handle3',
    '@handle4', '@handle5', '@handle6', '@handle7', '@handle8', '@handle9',"..."]

Limitations:
+ This only works for the first 5 pages of twitter handles. If there are more than this, you'll need to modify the code a bit
+ This only works where the whole altmetric page is accessible: you can't scrape handles where they are hidden behind the paywall
+ There is a 5 second delay between page loads (to be polite to the end site) you can modify/remove this, but you might be blocked.
+ I have only tested this for https://iop.altmetric.com, it may work for other publishers, but I haven't tried it.
+ This script *only* returns the people who tweeted themselves, it does not include the people they copied in to tweets, though you could probably add this functionality without too much bother if you really wanted to.

