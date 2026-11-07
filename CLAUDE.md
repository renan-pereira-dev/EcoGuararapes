# EcoGuararapes
Projeto de extensão (ADS/Wyden) sobre drenagem urbana e descarte irregular em Jaboatão dos Guararapes-PE.
Princípio orientador: primeiro construir um sistema confiável de coleta, privacidade, moderação e visualização; depois adicionar IA e modelos analíticos que possam ser avaliados com dados reais.

## Roadmap de Evolução
- **v1**: Reporte, banco, moderação e mapa (Next.js + Supabase + PostGIS)[cite: 1].
- **v2**: Triagem assistida por IA (FastAPI + API multimodal)[cite: 1].
- **v3**: Cruzamento de dados de chuva e análise (Pandas + scikit-learn)[cite: 1].
- **v4**: Modelo próprio de classificação de imagens (Hugging Face)[cite: 1].

## Regras de Código e Repositório
- Python 3.15.2, código simples e legível (padrão CS50P). Funções pequenas com docstrings.
- Use `git mv` para mover arquivos e preservar o histórico do repositório.
- **Privacidade Crítica**: Nunca commitar dados pessoais, imagens com metadados EXIF, ou coordenadas exatas de residências[cite: 1]. Ocultar rostos e placas.
- Commits no padrão Conventional Commits; textos técnicos e código em inglês.
- Antes de mudanças grandes, mostre o plano e espere minha aprovação.