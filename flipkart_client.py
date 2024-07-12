import json
import requests
from pydotmap import DotMap

class FlipkartClient:
    BASE_URL = "https://twitter.com/i/api/graphql/-oADiDXCeko8ztc6Vvth5Q/UserTweets"
    QUERYSTRING = {
        "variables": "{\"userId\":\"3502391593\",\"count\":1000,\"includePromotedContent\":true,\"withQuickPromoteEligibilityTweetFields\":true,\"withVoice\":true,\"withV2Timeline\":true}",
        "features": "{\"rweb_tipjar_consumption_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":true,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"communities_web_enable_tweet_community_results_fetch\":true,\"c9s_tweet_anatomy_moderator_badge_enabled\":true,\"articles_preview_enabled\":true,\"tweetypie_unmention_optimization_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"responsive_web_twitter_article_tweet_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"creator_subscriptions_quote_tweet_preview_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":true,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":true,\"rweb_video_timestamps_enabled\":true,\"longform_notetweets_rich_text_read_enabled\":true,\"longform_notetweets_inline_media_enabled\":true,\"responsive_web_enhance_cards_enabled\":false}",
        "fieldToggles": "{\"withArticlePlainText\":false}"
    }
    HEADERS = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "cookie": 'guest_id_marketing=v1%3A170993109384166555; guest_id_ads=v1%3A170993109384166555; guest_id=v1%3A170993109384166555; kdt=jbTAlNIR5inCvynf8mNyZJSJMp2rVKEXiGKCiokY; auth_token=faff2103dd67013f7b58eba3d141296b16cb1de8; ct0=1699c62bfa400cda9ff73b7f186d46a6e05c34910d6e357cb07e23c79800d86d351470dcd68bc01e1d1c653ccd6f3b4ce1f4d9f0e4b72549582484d9bd7953d0509d1fae85b84d684590ca7e58ab731e; twid=u%3D1180482654853951488; lang=en; personalization_id="v1_roDBfF023rw26WLZ0vzv0Q=="; external_referer=padhuUp37zj%2FMrVUnmTLd%2BLITvR%2FzYLWmODf04CXjfc%3D|0|GlWr2u5wzZipnVja1ZbglFG7jRzcDRbyNwPUPrWC%2FQdP%2FgWgNBa3L%2FyLdD1QNAQOom%2BodnCnKgxxrG3G44Rho3Tw0K9osiwouheVmJq6nAYveyuwkvvQvlyfJsuQ8rb5yqPq85%2BoPkj5EACiyOzsUg%3D%3D',
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://twitter.com/FlipkartStories",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-client-transaction-id": "wDxlqtAmTO9Xt56eTvERWIOo5qu6bfFvBg0iRJtpEkCuLP1wbU1CGN8infpZ1nUnIAQXgMLjCVvjrH+5eq3bz8/unEp3ww",
        "x-client-uuid": "36d8804c-4b8e-4324-baac-7f8ed4335c27",
        "x-csrf-token": "1699c62bfa400cda9ff73b7f186d46a6e05c34910d6e357cb07e23c79800d86d351470dcd68bc01e1d1c653ccd6f3b4ce1f4d9f0e4b72549582484d9bd7953d0509d1fae85b84d684590ca7e58ab731e",
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en"
    }

    def __init__(self):
        self.tweets_data = self.fetch_tweets()

    def fetch_tweets(self):
        try:
            response = requests.get(self.BASE_URL, headers=self.HEADERS, params=self.QUERYSTRING)
            response.raise_for_status()
            data = response.json()
            return data.get('data', {}).get('user', {}).get('result', {}).get('timeline_v2', {}).get('timeline', {}).get('instructions', [])[1].get('entries', [])
        except requests.RequestException as e:
            print(f"Failed to fetch tweets: {e}")
            return []
        except (KeyError, IndexError):
            print("Error parsing tweet data")
            return []

    def get_tweets(self):
        try:
            with open('data/flipkart_twitter.json', 'r') as f:
                tweets = json.load(f)
        except FileNotFoundError:
            tweets = {}

        for tweet in self.tweets_data:
            try:
                data = DotMap(tweet['content']['itemContent']['tweet_results']['result']['legacy'])
                tweets[data.id_str] = {    
                    'text': data.full_text,
                    'created_at': data.created_at,
                }
            except KeyError:
                continue
        return tweets
