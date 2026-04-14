from django.shortcuts import render
import random


def index(request):
    return render(request, 'index.html')


def result(request):
    name = request.GET.get('name', '익명')
    study = int(request.GET.get('study', 0) or 0)
    sleep = int(request.GET.get('sleep', 0) or 0)
    coffee = int(request.GET.get('coffee', 0) or 0)
    range_level = request.GET.get('range_level', 'medium')
    mindset = request.GET.get('mindset', 'normal')

    score = 50

    # 공부 시간
    if study <= 1:
        score += 20
    elif study <= 3:
        score += 10
    elif study <= 5:
        score += 0
    else:
        score -= 15

    # 수면 시간
    if sleep <= 3:
        score += 20
    elif sleep <= 5:
        score += 10
    elif sleep <= 7:
        score += 0
    else:
        score -= 5

    # 커피
    if coffee >= 5:
        score += 15
    elif coffee >= 3:
        score += 8
    elif coffee >= 1:
        score += 3

    # 시험 범위 체감
    if range_level == 'low':
        score -= 10
    elif range_level == 'medium':
        score += 0
    elif range_level == 'high':
        score += 15
    elif range_level == 'extreme':
        score += 25

    # 멘탈 상태
    if mindset == 'confident':
        score -= 10
    elif mindset == 'normal':
        score += 0
    elif mindset == 'bad':
        score += 10
    elif mindset == 'cry':
        score += 20

    # 랜덤 변수
    score += random.randint(-5, 5)

    # 0~100 제한
    score = max(0, min(score, 100))

    if score <= 20:
        level = '교수님도 인정할 안정권'
        messages = [
            '생각보다 괜찮습니다. 이번엔 진짜 준비했군요.',
            '이 정도면 시험지가 먼저 긴장할 차례입니다.',
            '당신의 생존 가능성은 매우 높습니다.'
        ]
        emoji = '😎'
        result_class = 'safe'

    elif score <= 40:
        level = '아슬아슬 생존형'
        messages = [
            '살 가능성은 있습니다. 하지만 자만은 금물입니다.',
            '지금부터 조금만 더 하면 훨씬 안전해집니다.',
            '벼랑 끝이긴 한데 아직 떨어지진 않았습니다.'
        ]
        emoji = '🙂'
        result_class = 'normal'

    elif score <= 60:
        level = '벼락치기 가능성 있음'
        messages = [
            '아직 끝난 건 아닙니다. 오늘 밤이 중요합니다.',
            '불안하지만 포기할 단계는 아닙니다.',
            '지금부터 집중하면 드라마 같은 전개가 가능합니다.'
        ]
        emoji = '😬'
        result_class = 'warning'

    elif score <= 80:
        level = '위험'
        messages = [
            '이제부터라도 정신 차리면 조금은 나아질 수 있습니다.',
            '현재 상황이 좋지는 않지만 기적은 늘 갑자기 옵니다.',
            '당신에게 필요한 건 산만함 차단과 빠른 집중입니다.'
        ]
        emoji = '😵'
        result_class = 'danger'

    else:
        level = '기도 메타 돌입'
        messages = [
            '지금 필요한 건 계산기가 아니라 기적입니다.',
            '현실을 마주할 시간이 가까워지고 있습니다.',
            '일단 책은 펴세요. 운명도 최소한의 노력은 원합니다.'
        ]
        emoji = '💀'
        result_class = 'doom'

    message = random.choice(messages)

    context = {
        'name': name,
        'score': score,
        'level': level,
        'message': message,
        'emoji': emoji,
        'result_class': result_class,
        'study': study,
        'sleep': sleep,
        'coffee': coffee,
    }

    return render(request, 'result.html', context)