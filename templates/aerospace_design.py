"""Finite, reviewed aerospace holiday layouts. No inferred product claims or LLM calls."""
import base64
import html

HOLIDAYS = {
 'space_day': ('中国航天日', '向星辰致意', '让探索的精神，抵达更远的地方', '04 / 24'),
 'mid_autumn': ('中秋节', '同望一轮月', '万里星河，共此团圆时', '中秋'),
 'national_day': ('国庆节', '山河同庆', '以探索之志，共赴新程', '10 / 01'),
 'new_year': ('元旦', '向新而行', '新的一年，继续仰望与探索', '01 / 01'),
 'spring_festival': ('春节', '星河迎新岁', '万家灯火，共启新程', '新春'),
}
VARIANTS = {
 'orbit': ('轨道 · 科技蓝', '克制的轨道线与信息层级，适合官网、技术品牌传播', '#081b2c', '#ecf6ff', '#77ddd6'),
 'editorial': ('远行 · 留白银', '大面积留白与纵向构图，适合企业公众号、合作伙伴祝福', '#f3f1e9', '#192e3e', '#b97934'),
 'celebration': ('共望 · 节庆红', '节庆色与天体轮廓结合，适合节日问候、客户关系维护', '#701f2c', '#fff2dc', '#e9b871'),
}

def options(profile):
    holiday, title, subtitle, date = HOLIDAYS[profile['holiday']]
    return [dict(id=k, name=v[0], rationale=v[1], title=title, subtitle=subtitle,
                 holiday=holiday, date=date, industry=profile['industry'],
                 brand=profile['brand'], bg=v[2], fg=v[3], accent=v[4]) for k,v in VARIANTS.items()]


def svg(profile, variant, image=b''):
    d = next(x for x in options(profile) if x['id'] == variant)
    e = lambda s: html.escape(str(s), quote=True)
    bg, fg, ac = d['bg'], d['fg'], d['accent']
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="{bg}"/>']
    def text(x,y,s,size=22,color=fg,extra=''):
        p.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif" font-size="{size}" {extra}>{e(s)}</text>')
    if variant == 'orbit':
        p.append(f'<g stroke="{ac}" opacity=".22" fill="none"><ellipse cx="978" cy="330" rx="270" ry="180" transform="rotate(-32 978 330)"/><ellipse cx="978" cy="330" rx="316" ry="228" transform="rotate(-32 978 330)"/><circle cx="978" cy="330" r="118"/><path d="M716 330H1240M978 62V606" stroke-dasharray="3 9"/></g>')
        tx,ty,ix,iy,iw,ih=72,285,808,163,376,335
    elif variant == 'editorial':
        p.append(f'<path d="M744 0V720" stroke="{ac}" opacity=".3"/><circle cx="1010" cy="285" r="185" fill="{ac}" opacity=".09"/><path d="M860 544L1170 70M878 555L1188 81" stroke="{ac}" opacity=".28"/>')
        tx,ty,ix,iy,iw,ih=72,302,820,128,370,375
    else:
        p.append(f'<circle cx="1010" cy="326" r="206" fill="{ac}" opacity=".94"/><circle cx="950" cy="268" r="174" fill="{bg}"/><g stroke="{ac}" fill="none" opacity=".22"><ellipse cx="990" cy="360" rx="289" ry="90" transform="rotate(-24 990 360)"/><path d="M70 130H1210M70 578H1210"/></g>')
        tx,ty,ix,iy,iw,ih=72,285,870,220,276,256
    if image:
        url='data:image/png;base64,'+base64.b64encode(image).decode()
        p.append(f'<image x="{ix}" y="{iy}" width="{iw}" height="{ih}" href="{url}" preserveAspectRatio="xMidYMid meet"/>')
    elif profile['industry']=='satellite':
        p.append(f'<g transform="translate(990 330) rotate(-22)" stroke="{ac if variant != "celebration" else fg}" stroke-width="2" fill="{bg}"><rect x="-27" y="-43" width="54" height="86"/><path d="M-27 0H-147M27 0H147M0-43V-78M-16-78H16"/><rect x="-170" y="-34" width="130" height="68"/><rect x="40" y="-34" width="130" height="68"/><path d="M-128-34V34M-84-34V34M83-34V34M126-34V34M-170 0H-40M40 0H170"/></g>')
    else:
        p.append(f'<g transform="translate(992 350) rotate(22)" stroke="{ac if variant != "celebration" else fg}" stroke-width="2" fill="{bg}"><path d="M-30 88V-70Q-30-130 0-165Q30-130 30-70V88ZM-30 28L-60 87H-30M30 28L60 87H30M-20 100L0 162L20 100"/><path d="M-30-50H30M-30 50H30"/></g>')
    text(72,76,profile['brand'],min(25,900/max(1,len(profile['brand']))),extra='letter-spacing="2"')
    text(72,164,d['holiday'],19,ac,extra='letter-spacing="5"')
    text(tx,ty,d['title'],min(82,610/max(1,len(d['title']))),extra='font-weight="500" letter-spacing="2"')
    p.append(f'<path d="M72 {ty+40}H130" stroke="{ac}" stroke-width="3"/>')
    text(72,ty+98,d['subtitle'],26)
    text(72,537,'致每一位同行者',19,ac)
    p.append(f'<path d="M72 615H1208" stroke="{ac}" opacity=".35"/>')
    text(72,658,('卫星' if profile['industry']=='satellite' else '火箭')+' · '+d['holiday'],17)
    text(1208,658,d['date'],18,ac,extra='text-anchor="end" letter-spacing="4"')
    if not image:
        text(1208,591,'概念示意 · 非产品实拍',13,fg,extra='text-anchor="end" opacity=".65"')
    p.append('</svg>')
    return ''.join(p)
