from datetime import datetime
from django.shortcuts import render, redirect
from .models import DaySchedule


# ─── All UI strings, both languages ──────────────────────────────────────────
TRANSLATIONS = {
    "ru": {
        "lang_switch_label": "Кыргызча",
        "lang_switch_code": "ky",
        "hero_tagline": "⚡ Экстренный выезд — 7 дней в неделю",
        "hero_subtitle": "Коммерческий и бытовой ремонт холодильного оборудования и кондиционеров.",
        "hero_slogan": "Быстро. Надёжно. Холодно.",
        "stat_employees": "сотрудников",
        "stat_years": "года на рынке",
        "stat_orders": "заявок в день",
        "on_duty_label": "📞 На смене сегодня",
        "no_operator": "Оператор не назначен.",
        "no_operator_sub": "Попробуйте позже или позвоните на основную линию.",
        "services_title": "Что мы",
        "services_title_hl": "ремонтируем",
        "services_sub": "Если должно быть холодно, а там тепло — мы это исправим.",
        "why_title": "Почему",
        "why_title_hl": "выбирают нас",
        "why_items": [
            {"icon": "🏆", "title": "3+ года опыта",           "desc": "Работаем на рынке с 2022 года. Сотни довольных клиентов по всему городу."},
            {"icon": "👷", "title": "50+ специалистов",        "desc": "Сертифицированные мастера по всем видам холодильного оборудования и кондиционеров."},
            {"icon": "⚡", "title": "Выезд день в день",       "desc": "Принимаем заявки 7 дней в неделю и выезжаем в день обращения."},
            {"icon": "🔧", "title": "Гарантия на работы",      "desc": "Даём письменную гарантию на все виды выполненных ремонтных работ."},
            {"icon": "📦", "title": "Оригинальные запчасти",   "desc": "Используем только сертифицированные детали и расходные материалы."},
            {"icon": "💰", "title": "Честные цены",            "desc": "Диагностика бесплатно. Стоимость озвучиваем строго до начала ремонта."},
        ],
        "schedule_title": "Расписание",
        "schedule_title_hl": "на неделю",
        "schedule_sub": "Полная прозрачность — знайте, кто на смене, ещё до звонка.",
        "col_day": "День",
        "col_operator": "Оператор",
        "col_phone": "Телефон",
        "badge": "НА СМЕНЕ",
        "footer_copy": "CoolFix Ремонт. Все права защищены.",
    },
    "ky": {
        "lang_switch_label": "Русча",
        "lang_switch_code": "ru",
        "hero_tagline": "⚡ Шашылыш чыгуу — жумасына 7 күн",
        "hero_subtitle": "Коммерциялык жана турмуштук муздаткыч жабдуулар жана кондиционерлерди оңдоо.",
        "hero_slogan": "Тез. Ишенимдүү. Муздак.",
        "stat_employees": "кызматкер",
        "stat_years": "жыл рынокто",
        "stat_orders": "буйрутма күн сайын",
        "on_duty_label": "📞 Бүгүн кезматта",
        "no_operator": "Оператор дайындалган эмес.",
        "no_operator_sub": "Кийинчерээк байланышыңыз же негизги линияга чалыңыз.",
        "services_title": "Эмнени",
        "services_title_hl": "оңдойбуз",
        "services_sub": "Муздак болушу керек болсо, а ысык болсо — биз оңдойбуз.",
        "why_title": "Эмне үчүн",
        "why_title_hl": "бизди тандайт",
        "why_items": [
            {"icon": "🏆", "title": "3+ жыл тажрыйба",        "desc": "2022-жылдан бери иштейбиз. Шаар боюнча жүздөгөн канааттанган кардарлар."},
            {"icon": "👷", "title": "50+ адис",                "desc": "Бардык муздаткыч жабдуулары жана кондиционерлер боюнча сертификатталган чеберлер."},
            {"icon": "⚡", "title": "Ошол күнү чыгабыз",      "desc": "Жумасына 7 күн кабыл алабыз жана кайрылган күнү чыгабыз."},
            {"icon": "🔧", "title": "Иштерге кепилдик",       "desc": "Бардык аткарылган ремонттук иштерге жазуу жүзүндө кепилдик беребиз."},
            {"icon": "📦", "title": "Оригинал запчасттар",    "desc": "Сертификатталган бөлүктөр жана керек-жарактарды гана колдонобуз."},
            {"icon": "💰", "title": "Адилет баалар",          "desc": "Диагностика акысыз. Ремонттун баасын иштен мурун айтабыз."},
        ],
        "schedule_title": "Жумалык",
        "schedule_title_hl": "иш графиги",
        "schedule_sub": "Толук ачыктык — чалардан мурун кимдин кезматта экенин билиңиз.",
        "col_day": "Күн",
        "col_operator": "Оператор",
        "col_phone": "Телефон",
        "badge": "КЕЗМАТТА",
        "footer_copy": "CoolFix Оңдоо. Бардык укуктар корголгон.",
    },
}

# ─── Services (translatable, structured separately from UI strings) ──────────
SERVICES = {
    "ru": [
        {"icon": "🧊", "title": "Холодильники и морозильники",           "desc": "Бытовые и коммерческие агрегаты любых марок"},
        {"icon": "❄️", "title": "Холодильные камеры и рефрижераторы",    "desc": "Крупногабаритное промышленное оборудование"},
        {"icon": "🥤", "title": "Витринные и барные холодильники",        "desc": "Ларевые морозильники и торговые витрины"},
        {"icon": "💨", "title": "Кондиционеры",                          "desc": "Ремонт бытовых и промышленных кондиционеров"},
    ],
    "ky": [
        {"icon": "🧊", "title": "Муздаткычтар жана морозильниктер",         "desc": "Каалаган маркадагы турмуштук жана коммерциялык агрегаттар"},
        {"icon": "❄️", "title": "Муздак камералар жана рефрижераторлор",    "desc": "Ири өнөр жай жабдуулары"},
        {"icon": "🥤", "title": "Витриналык жана бар муздаткычтары",        "desc": "Ларь морозильниктер жана соода витриналары"},
        {"icon": "💨", "title": "Кондиционерлер",                          "desc": "Турмуштук жана өнөр жай кондиционерлерин оңдоо"},
    ],
}

# ─── Day names — annotated onto schedule objects in Python, not in template ──
DAY_NAMES = {
    "ru": {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"},
    "ky": {1: "Дүйшөмбү",   2: "Шейшемби", 3: "Шаршемби", 4: "Бейшемби", 5: "Жума", 6: "Ишемби", 7: "Жекшемби"},
}


def set_language(request, lang: str):
    """Flip the session language and bounce back to home. Dead simple."""
    if lang in ("ru", "ky"):
        request.session["lang"] = lang
    return redirect("home")


def home(request):
    today_num = datetime.now().isoweekday()
    lang = request.session.get("lang", "ru")  # Russian by default

    # One DB hit for 7 rows — reused for both hero card and schedule table
    schedules = list(
        DaySchedule.objects.select_related("operator").order_by("day_of_week")
    )

    # Stamp localized day name directly onto each object — zero extra queries
    day_names = DAY_NAMES[lang]
    for s in schedules:
        s.day_label = day_names[s.day_of_week]

    today_schedule = next((s for s in schedules if s.day_of_week == today_num), None)

    return render(request, "core/index.html", {
        "schedules": schedules,
        "today_schedule": today_schedule,
        "today_num": today_num,
        "services": SERVICES[lang],
        "t": TRANSLATIONS[lang],
        "lang": lang,
    })