# FAQ 

*Mostly questions I've been frequently asking myself.*

## Is this practical? Or just a toy?

When I started the project I mostly assumed it was a toy. But I've been surprised by the results.

After my initial GPT-4 experiments, [Simon Willison asked](https://mastodon.social/@simon@simonwillison.net/110042216119791967) how well it'd work on GPT-3.5-turbo. I hadn't realized the significant price difference, and without switching to 3.5-turbo, I'd probably have decided it was too expensive to be practical.

Once I realized 3.5-turbo was an option, I was able to spend a lot more time tinkering with the prompt and token reduction.  It also got me thinking more about what kind of tooling you'd want around something like this if you were going to actually use it.

## Why would I use this instead of a traditional scraper?

It is definitely great for quick prototypes and ad-hoc data extraction. The CLI tool allows you to initiate a scraping session with a *single command* without writing any code, making it ideal for rapid testing and development.

Advantages over traditional scrapers are several-fold:

- **Flexibility in Unstructured Data Handling**: Traditional scrapers rely on fixed patterns or selectors, which may fail when a website changes. `scrapeghost`'s model-based approach is adept at interpreting unstructured data and adapts more gracefully to changes in page structure.

- **Ease of Use for Non-Developers**: The ability to use natural language instructions makes `scrapeghost` more accessible to those without extensive programming or web scraping experience.

- **Speed of Deployment**: Setting up `scrapeghost` is faster compared to writing a full-fledged scraper, saving valuable time especially when dealing with simple or one-off scraping tasks.

However, there are also challenges and limitations to consider:

- **Costs of API Usage**: While it can be efficient in terms of development time, costs can accumulate with extensive use of the API, especially for larger or more complex scraping tasks.

- **Opaque Errors**: Troubleshooting is made harder by less transparent error messages, which could hinder understanding of why certain extractions fail.

- **Dependence on Upstream Provider**: The reliance on OpenAI's models means any changes in their API, pricing, or availability can directly impact your scraping capabilities.
This means you don't need to sink a bunch of time into deciding if it's worth it or not.

Or, imagine a scraper that needs to run infrequently on a page that is likely to break in subtle ways between scrapes.
A CSS/XPath-based scraper will often be broken in small ways between the first run and another run months later, there's a decent chance that those changes won't break a GPT-based scraper.

It is also quite good at dealing with unstructured text. A list of items in a sentence can be hard to handle with a traditional scraper, but GPT handles many of these cases without much fuss.

## What are the disadvantages?

* It is terrible at pages that are large lists (like a directory), they need to be broken into multiple chunks and the API calls can be expensive in terms of time and money.
* It is opaque.  When it fails, it can be hard to tell why.
* If the page is dynamic, this approach won't work at all.  It requires all of the content to be available in the HTML.
* It is *slow*.  A single request can take over a minute if OpenAI is slow to respond.
* Right now, it only works with OpenAI, that means you'll be dependent on their pricing and availability. It also means
you need to be comfortable sending your data to a third party.


## Why not use a different model?

See <https://github.com/jamesturk/scrapeghost/issues/18>.

## Can I use `httpx`? Or `selenium`/`playwright`? Can I customize the headers, etc.?

This library is focused on handling the HTML that's already been retrieved.  There's no reason you can't use any of these libraries to retrieve the HTML.  The `scrape` method accepts either a URL or a string of already fetched HTML.

If you'd like to use another library, do it as you usually would, but instead of passing the HTML to `lxml.html` or `BeautifulSoup`, pass it to `scrapeghost`.

## What can I do if a page is too big?

Dealing with large pages requires a strategy that includes scoping and preprocessing. Here are some steps and examples to help you effectively handle large pages:

1. Use CSS or XPath selectors to narrow the focus of the page to significant areas. For example:
- CSS: Use `.main-content` to target the main content area.
- XPath: Use `//div[@class='product-list']/div` to select only the product list items.

2. Pre-process the HTML by removing unnecessary sections, tags, or irrelevant data to streamline the scraping process. This could involve:
- Stripping out `<script>` and `<style>` tags.
- Removing comments or non-essential metadata.
- Simplifying the DOM structure by eliminating redundant wrappers.
Utilize the library's preprocessing features to automate such tasks wherever possible.

3. Finally, you can use the `auto_split_length` parameter to split the page into smaller chunks.  This only works for list-type pages, and requires a good choice of selector to split the page up.

## Why not ask the scraper to write CSS / XPath selectors?

While it'd seem like this would perform better, there are a few practical challenges standing in the way right now.

* Writing a robust CSS/XPath selector that'd run against a whole set of pages would require passing a lot of context to the model. The token limit is already the major limitation.
* The current solution does not require any changes when a page changes.  A selector-based model would require retraining every time a page changes as well as a means to detect such changes.
* For some data, selectors alone are not enough. The current model can easily extract all of the addresses from a page and break them into city/state/etc. A selector-based model would not be able to do this.

I do think there is room for hybrid approaches, and I plan to continue to explore them.

## Does the model "hallucinate" data?

It is possible, but in practice hasn't been observed as a major problem yet.

Because the [*temperature*](https://platform.openai.com/docs/api-reference/completions) is zero, the output is fully deterministic and seems less likely to hallucinate data.

The `HallucinationChecker` class can be used to detect data that appears in the response that doesn't appear on the page. This approach could be improved, but I haven't seen hallucination as a major problem yet.  (If you have examples, please open an issue!)

## How much did you spend developing this?

So far, the expenditure on API calls is approximately $40, which reflects careful management of the tool's functionality to minimize costs.

Cost-Control Strategies:

- **Max Cost Limiting**: It's possible to set a maximum cost at which the scraping tool will stop processing, ensuring that you never exceed your budget. For instance, a GPT-4 call that would normally cost $2.20 can be limited to a lower threshold.

- **Selective Scraping**: Preprocess the HTML to target only the essential content or use split strategies to efficiently distribute API calls across sections of a page.

- **Efficiency Adjustments**: Switching to models like GPT-3.5 can significantly reduce costs, providing a balance between performance and affordability. Optimization of prompts and careful configuration of tool parameters can also help keep the costs in check.

- **Cost Tracking**: Keeping a close eye on the expenditure and adjusting your scraping strategy allows for incremental improvement in both cost-efficiency and the quality of results.

These examples illustrate how integral cost management is to the sustainable use of scraping tools and highlight the importance of understanding and utilizing cost-limiting features.

## What's with the license?

I'm still working on figuring this out.

For now, if you're working in a commercial setting and the license scares you away, that's fine.

If you really want to, you can contact me and we can work something out.