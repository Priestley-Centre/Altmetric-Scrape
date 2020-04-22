# Altmetric-Scrape
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Priestley-Centre/Altmetric-Scrape?include_prereleases)](https://github.com/Priestley-Centre/Altmetric-Scrape/releases/tag/v1.0)
[![GitHub](https://github.com/RollsW/Altmetric-Scrape/blob/master/docs/MIT.svg)](https://github.com/RollsW/Altmetric-Scrape/blob/master/docs/LICENSE)
[![Code style: black](https://github.com/RollsW/Altmetric-Scrape/blob/master/docs/black.svg)](https://github.com/psf/black)

Here's the story. I was about to submit an article to an IOP journal. It referred quite a lot to another paper published in the same journal, which had already been talked about on twitter. I needed a way to contact all the tweeps that talked about it before, to let them know that the paper cast a new light on what they had shared.

This (very simple) python script consists of a two functions which check the [altmetric](https://www.altmetric.com/) page for a paper and returns either, all the twitter handles as a de-duplicated list, or links to all the tweets where the paper is mentioned.

for example: `scrape_handles("https://iop.altmetric.com/details/5152221/")`

returns: `['@handle0', '@handle1', '@handle2', '@handle3', '@handle4', '@handle5', '@handle6'...]`

and: `scrape_links("https://iop.altmetric.com/details/5152221/")`

returns: `['url0', 'url1', 'url2', 'url3', 'url4', 'url5', 'url6'...]`

Limitations:
+ This only works for the first 5 pages of twitter handles. If there are more than this, you'll need to modify the code a bit(just change the n value for the `while` loop in each function
+ This only works where the whole altmetric page is accessible: you can't scrape handles where they are hidden behind the paywall
+ There is a 5 second delay between page loads (to be polite to the end site) you can modify/remove this, but you might be blocked.
+ I have only tested this for https://iop.altmetric.com, it may work for other publishers, but I haven't tried it.
+ This script *only* returns the people who tweeted themselves, it does not include the people they copied in to tweets, though you could probably add this functionality without too much bother if you really wanted to.

