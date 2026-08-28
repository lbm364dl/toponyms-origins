#!/usr/bin/env python3
"""Shared publication-quality checks for reader-facing station copy."""

from __future__ import annotations

import re


SPANISH_PUBLIC_TONE_RULES = (
    (
        'references draft or previous wording',
        re.compile(
            r'\b(?:la|esta|una) (?:redacción|versión|explicación|afirmación|interpretación) '
            r'(?:actual|existente|de partida|original|anterior)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'references a public/editorial deliverable',
        re.compile(
            r'\b(?:para|en) (?:una|la) (?:explicación|interpretación|redacción|presentación|versión|ficha|cartela) pública\b'
            r'|\bde cara al público\b|\bpara (?:la|una|esta) ficha\b',
            re.IGNORECASE,
        ),
    ),
    (
        'instructs an editor instead of stating the evidence',
        re.compile(
            r'\b(?:conviene|debe|debería) (?:\w+\s+){0,3}'
            r'(?:consultar|revisar|comprobar|decir|presentar(?:la|lo|las|los)?|presentarse|formular(?:la|lo|las|los)?|formularse|tratar(?:la|lo|las|los)?|tratarse|explicar(?:la|lo|las|los)?|explicarse|corregir(?:la|lo|las|los)?|corregirse|aclarar(?:la|lo|las|los)?|evitar|matizar|precisar|mencionar)\b'
            r'|\bpuede (?:presentarse|formularse|tratarse|explicarse|corregirse)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'uses first-person research narration',
        re.compile(
            r'\b(?:no |tampoco )?(?:he|hemos) '
            r'(?:encontrado|localizado|comprobado|revisado|consultado|investigado|podido)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'reports the research process',
        re.compile(
            r'\bno se (?:ha )?(?:encontrado|localizado|podido confirmar|podido verificar)\b'
            r'|\b(?:durante|en) (?:esta|la presente) investigación\b',
            re.IGNORECASE,
        ),
    ),
    (
        'leaves an editorial task pending',
        re.compile(
            r'\b(?:queda|quedan|está|están|sigue|siguen) (?:aún )?'
            r'(?:pendiente(?:s)? de|por) '
            r'(?:confirmar|comprobar|revisar|localizar|documentar|verificar|una fuente)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'describes an editorial correction or formulation',
        re.compile(
            r'\b(?:la|una) (?:corrección|formulación) '
            r'(?:principal|más importante|prudente|segura|sólida|adecuada)\b',
            re.IGNORECASE,
        ),
    ),
)

ENGLISH_PUBLIC_TONE_RULES = (
    (
        'references draft or previous wording',
        re.compile(
            r'\b(?:the|this) (?:current|existing|previous|original) '
            r'(?:draft|wording|copy|explanation|claim|text)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'references a public/editorial deliverable',
        re.compile(
            r'\bfor (?:the|a|this) (?:card|entry|page|public version|public explanation)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'instructs an editor instead of stating the evidence',
        re.compile(
            r'\b(?:should|must|needs? to) (?:be )?'
            r'(?:presented|phrased|worded|written|explained|treated|corrected|revised|removed|kept|clarified)\b',
            re.IGNORECASE,
        ),
    ),
    (
        'uses first-person research narration',
        re.compile(
            r"\b(?:I|we) (?:have )?(?:found|located|checked|reviewed|consulted|researched|couldn't find|could not find)\b",
            re.IGNORECASE,
        ),
    ),
    (
        'reports the research process',
        re.compile(r'\b(?:during|in) this research\b', re.IGNORECASE),
    ),
)


def public_tone_issues(text: object, language: str = 'es') -> list[tuple[str, str]]:
    """Return unique tone-rule labels and matched excerpts for public copy."""
    value = str(text or '')
    rules = ENGLISH_PUBLIC_TONE_RULES if language == 'en' else SPANISH_PUBLIC_TONE_RULES
    issues: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for label, pattern in rules:
        for match in pattern.finditer(value):
            issue = (label, match.group(0))
            if issue not in seen:
                seen.add(issue)
                issues.append(issue)
    return issues
