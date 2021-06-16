# Summary of project purpose and goal

I've had a hard time finding work in my field in the recent months and started working at my local pet store to cover the bills. I noticed that we only had a less than highly organized and put together paper system to keep track of backstock, and thought that it might be a fun side project to put something together in a a couple afternoons to have a good mobile website for viewing and updating what is available in backstock. All user accounts can view the inventory items and their quantities, staff accounts can do that as well as change quantities, and manager accounts can do all of that as well as add or remove items.

I think it's highly unlikely the store will put this into use because for one thing they most likely wouldn't want to essentially require employees to have a cell phone with them and on top of that it isn't the most incredible looking site. In addition to aesthetic pitfalls theres a few issues with functionality that I can think of on the spot. 

The first being that if any post method is called such as adding or removing an item or changing a quantity the 'persistent' filter options will reset to all brands and all categories, and also that each filter change requires a post method that reloads the page. I think that in a real well put together project I would pass more information in on initial load and then handle more operations like filtering with a select menu through strictly javascript to speed up the process. For the problem of dropping the filters I know one solution would be making the filters an actual url resolved queryset but for the time being I didn't want to spend more time than making one url path that resolves each way.

The second problem I can think of is that you have to update each item's quantity one at a time with a post method required after which will reload the page. Where the other problems I had an answer to that I just didn't want to spend the amount of time required to put in place, I'm not entirely sure I have an answer for this problem. My best idea would be making the entire set of products one form instead of them each being there own, and then including a data tag on each quantity and delete button to specify the product they go to and then iterating over each item to update as necessary on a post method. I believe that would work but may be prone to causing other issues.
