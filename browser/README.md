# AgentCore Browser Demo

Examples on Using AgentCore Browser.

For details, please refer to my blog: [Bedrock AgentCore Part4: Browser for Web Application Interactions!](https://medium.com/@itsuki.enjoy/bedrock-agentcore-part4-browser-for-web-application-interactions-6b0593de39b5)

## Demos Included
1. [Basic usage](./basic_usage_playwright.ipynb)
    - Demo the basic usage of AgentCore Browser with Playwright automation framework to programmatically control and interact with browser.
3. [Browser with Recording & Replay](./session_recording_replay.ipynb)
    - Create A custom Browser that supports stroing recordings in Amazon S3. This feature enables us to review past browser interactions for debugging, auditing, or training purposes. The recordings in S3 include DOM change events, browser network activity, and console logs for comprehensive session analysis.
    - Run some sample sessions, retrieve the recording from S3, and process the recording events.
    - Stop all the running session and delete the browser
