import re


keywords = {'c#', '.net', 'python', 'node.js', 'php', 'git'}

description = "Building mr concerns servants in he outlived am breeding. He so lain good miss when sell some at if. Told hand so an rich gave next. How c# doubt yet again see son smart. While mirth large of on front. Ye he greater related adapted proceed entered an. Through it examine express promise no. Past add size game cold girl off how old. Sense child do state to defer mr of forty. Become latter but nor abroad wisdom waited. Was delivered gentleman acuteness but daughters. In as of whole as match asked. Pleasure exertion put add entrance distance drawings. In equally matters showing greatly it as. Want c# name any wise are able park when. Saw vicinity python judgment remember finished men throwing. He as compliment unreserved projecting. Between had observe pretend delight for believe. Do newspaper questions consulted sweetness node.js do. Our sportsman his unwilling fulfilled departure law. Now world own total saved above her cause table. Wicket myself her square remark the should far secure sex. Smiling cousins warrant law explain for whether. Sudden she seeing garret far c# regard. By hardly it direct if pretty up regret. Ability thought enquire settled prudent you sir. Or easy knew sold on well come year. Something consulted age extremely end procuring. Collecting preference he inquietude projection me php in by. So do of sufficient projecting an thoroughly uncommonly prosperous conviction. Pianoforte principles our unaffected not for astonished travelling are particular. Was drawing natural fat respect husband. An as noisy an offer drawn blush place. These tried for way joy wrote witty. In mr began music weeks after at begin. Education no dejection so direction pretended household do .net to. Travelling everything her eat reasonable c# unsatiable decisively simplicity. Morning request be lasting it fortune demands highest of. Surrounded affronting favourable no mr. Lain knew like half she yet joy. Be than dull as seen very shot. Attachment node.js ye so am travelling estimating projecting is. Off fat address attacks his besides. Suitable settling mr attended no doubtful feelings. Any over for say bore such sold five but hung. Drawings me opinions returned absolute in. Otherwise therefore sex did are unfeeling something. Certain be ye amiable by exposed so. To celebrated estimating python excellence do. Coming either suffer living her gay theirs. Furnished do otherwise daughters contented conveying attempted no. Was yet general visitor present hundred too c# brother fat arrival. Friend are day own either lively new. Procuring education on consulted assurance in do. Is sympathize he expression mr no travelling. Preference he he at travelling in resolution. So striking at of to welcomed resolved. Northward by described up household therefore python attention. Excellence decisively nay man yet impression for contrasted .net remarkably. There spoke happy for you are out. Fertile how old address did showing because sitting replied six. Had arose guest visit going off child she new. Adieus except say barton put feebly favour him. Entreaties unpleasant sufficient few pianoforte discovered uncommonly ask. Morning cousins .net amongst in mr weather do neither. Warmth object matter course active law spring six. Pursuit showing tedious unknown winding see had man add. And park eyes too more him. Simple excuse active had son wholly coming number add. Though all excuse ladies rather regard assure yet. If feelings so prospect no as raptures quitting. Examine she brother prudent add day ham. Far stairs now coming bed oppose hunted become his. You zealously departure had procuring suspicion. Books .net whose front would purse if be do decay. Quitting you way formerly disposed perceive ladyship are. Common turned boy direct and yet."

def find_keywords(keywords, description):
    keywords_present = set()

    for keyword in keywords:
        # escapes special regex characters in keywords like 'c#' & '.net"
        escaped_keyword = re.escape(keyword)
        # handles word boundaries as well as keywords like 'c#' and '.net'
        pattern = r'(?:^|[^\w]){}(?:$|[^\w])'.format(escaped_keyword)

        if re.search(pattern, description):
            keywords_present.add(keyword)

    return keywords_present


print(find_keywords(keywords, description))
