# YouTube Growth Tools

Practical Python tools to help you analyze your channel, score content, and optimize for growth.

## Available Tools

### 1. Content Performance Analyzer (`content_performance_analyzer.py`)

Analyzes your YouTube channel's content performance to identify patterns and opportunities.

**Features:**
- Performance analysis by content type
- Performance analysis by topic
- Top performer identification
- Underperformer identification
- Engagement rate calculation
- Actionable recommendations

**Usage:**
```bash
python content_performance_analyzer.py
```

**Input Format:**
Create a CSV file named `content_data.csv` with the following columns:
- title
- content_type
- topic
- views
- watch_time
- likes
- comments
- subscribers_gained
- upload_date

**Output:**
- Console report with analysis
- `analysis_results.json` with detailed results

---

### 2. Content Scorer (`content_scorer.py`)

Scores your YouTube videos before publishing to predict performance.

**Features:**
- 8-dimension scoring framework
- Weighted scoring system
- Performance prediction
- Improvement suggestions
- Interactive scoring interface

**Usage:**
```bash
python content_scorer.py
```

**Scoring Dimensions:**
1. Content Quality (15% weight)
2. Title Optimization (15% weight)
3. Thumbnail Optimization (15% weight)
4. SEO Optimization (10% weight)
5. Audience Alignment (15% weight)
6. Engagement Potential (10% weight)
7. Competitive Positioning (10% weight)
8. Production Value (10% weight)

**Output:**
- Detailed score report
- Grade and recommendation
- Weak dimension identification
- Improvement suggestions
- Optional JSON export

---

## Installation

These tools require Python 3.7+. No external dependencies required (uses only standard library).

```bash
# No installation needed - just run the scripts!
python content_performance_analyzer.py
python content_scorer.py
```

---

## Getting Your Data

### For Content Performance Analyzer

Export your YouTube Analytics data:

1. Go to YouTube Studio → Analytics
2. Click "Advanced mode"
3. Select date range (last 90 days recommended)
4. Export to CSV
5. Format according to expected CSV structure
6. Save as `content_data.csv` in the tools directory

### For Content Scorer

No data needed - this is an interactive tool that prompts you for scores.

---

## Tips

- **Regular Analysis:** Run the performance analyzer monthly to track trends
- **Pre-Publish Scoring:** Score every video before publishing
- **Track Improvements:** Compare scores over time to measure improvement
- **Combine with Creator Unlock:** Use these tools alongside [Creator Unlock](https://creatorunlock.com?fpr=chris95) for comprehensive analysis

---

## Contributing

Found a bug or want to add a feature? Contributions welcome!

1. Fork the repository
2. Make your changes
3. Submit a pull request

---

## Related Resources

- [Channel Audits Guide](../guides/channel-audits.md)
- [Content Scoring Guide](../guides/content-scoring.md)
- [Creator Unlock](https://creatorunlock.com?fpr=chris95) - AI-powered YouTube growth platform

