def to_json_user(redditor):
    json = {
                'name': redditor.name,
                'comment_karma': redditor.comment_karma,
                'id': redditor.id,
                'link_karma': redditor.link_karma
            }
    return json


def to_json_post(post, show_body=False):
    json = {
                'author': str(post.author),
                'title': str(post.title),
                'score': str(post.score),
                'id': str(post.id),
                'num_comments': str(post.num_comments),
                'created_utc': str(post.created_utc)
            }
    if show_body:
        json['body'] = post.selftext
    return json


def to_json_comment(comment):
    json = {
                'author': str(comment.author),
                'body': str(comment.body),
                'score': str(comment.score),
                'id': str(comment.id),
                'created_utc': str(comment.created_utc)
            }
    return json
