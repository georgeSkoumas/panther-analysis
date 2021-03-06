def rule(event):
    return (event['eventName'] == 'ConsoleLogin' and
            event['userIdentity'].get('type') == 'IAMUser' and
            event.get('responseElements', {}).get('ConsoleLogin') == 'Failure')


def dedup(event):
    return event['userIdentity'].get('arn')
