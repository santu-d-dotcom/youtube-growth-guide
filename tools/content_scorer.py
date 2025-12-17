"""
Content Scoring Tool
Scores YouTube videos before publishing to predict performance.

Usage:
    python content_scorer.py
"""

import json
from typing import Dict


class ContentScorer:
    """Scores content across multiple dimensions to predict performance."""
    
    def __init__(self):
        self.dimensions = {
            'content_quality': {
                'weight': 0.15,
                'description': 'Value, uniqueness, production quality, accuracy'
            },
            'title_optimization': {
                'weight': 0.15,
                'description': 'Keywords, CTR potential, clarity, length'
            },
            'thumbnail_optimization': {
                'weight': 0.15,
                'description': 'Visual appeal, CTR potential, brand consistency, mobile optimization'
            },
            'seo_optimization': {
                'weight': 0.10,
                'description': 'Description, tags, keywords, metadata'
            },
            'audience_alignment': {
                'weight': 0.15,
                'description': 'Matches expectations, addresses needs, difficulty level, relevance'
            },
            'engagement_potential': {
                'weight': 0.10,
                'description': 'Hook effectiveness, CTAs, interaction opportunities, shareability'
            },
            'competitive_positioning': {
                'weight': 0.10,
                'description': 'Differentiation, value proposition, market timing, trend alignment'
            },
            'production_value': {
                'weight': 0.10,
                'description': 'Video quality, audio quality, editing quality, overall polish'
            }
        }
    
    def score_dimension(self, dimension: str, score: int) -> Dict:
        """Score a single dimension."""
        if score < 1 or score > 10:
            raise ValueError(f"Score must be between 1 and 10, got {score}")
        
        if dimension not in self.dimensions:
            raise ValueError(f"Unknown dimension: {dimension}")
        
        weight = self.dimensions[dimension]['weight']
        weighted_score = score * weight
        
        return {
            'dimension': dimension,
            'score': score,
            'weight': weight,
            'weighted_score': weighted_score,
            'description': self.dimensions[dimension]['description']
        }
    
    def score_content(self, scores: Dict[str, int]) -> Dict:
        """Score content across all dimensions."""
        results = {}
        total_weighted_score = 0
        total_score = 0
        
        # Score each dimension
        for dimension, score in scores.items():
            if dimension in self.dimensions:
                dimension_result = self.score_dimension(dimension, score)
                results[dimension] = dimension_result
                total_weighted_score += dimension_result['weighted_score']
                total_score += score
        
        # Calculate averages
        num_dimensions = len(results)
        average_score = total_score / num_dimensions if num_dimensions > 0 else 0
        
        # Determine grade
        if average_score >= 9:
            grade = 'A+'
            recommendation = 'Excellent - Publish with confidence'
        elif average_score >= 8:
            grade = 'A'
            recommendation = 'Very Good - Minor optimizations recommended'
        elif average_score >= 7:
            grade = 'B'
            recommendation = 'Good - Some optimizations recommended'
        elif average_score >= 6:
            grade = 'C'
            recommendation = 'Average - Several optimizations needed'
        elif average_score >= 5:
            grade = 'D'
            recommendation = 'Below Average - Significant improvements required'
        else:
            grade = 'F'
            recommendation = 'Poor - Major overhaul needed before publishing'
        
        # Identify weak dimensions
        weak_dimensions = [
            dim for dim, result in results.items()
            if result['score'] < 6
        ]
        
        # Identify strong dimensions
        strong_dimensions = [
            dim for dim, result in results.items()
            if result['score'] >= 8
        ]
        
        return {
            'total_score': total_score,
            'average_score': round(average_score, 2),
            'weighted_score': round(total_weighted_score, 2),
            'grade': grade,
            'recommendation': recommendation,
            'dimensions': results,
            'weak_dimensions': weak_dimensions,
            'strong_dimensions': strong_dimensions,
            'max_possible_score': 80,
            'score_percentage': round((total_weighted_score / 1.0) * 100, 2)
        }
    
    def print_score_report(self, scoring_result: Dict):
        """Print a formatted score report."""
        print("\n" + "="*80)
        print("CONTENT SCORING REPORT")
        print("="*80)
        
        print(f"\nOverall Score: {scoring_result['average_score']}/10")
        print(f"Grade: {scoring_result['grade']}")
        print(f"Score Percentage: {scoring_result['score_percentage']}%")
        print(f"\nRecommendation: {scoring_result['recommendation']}")
        
        print("\n" + "-"*80)
        print("DIMENSION SCORES")
        print("-"*80)
        print(f"\n{'Dimension':<30} {'Score':<10} {'Weight':<10} {'Weighted':<10}")
        print("-"*80)
        
        for dimension, result in scoring_result['dimensions'].items():
            dim_name = dimension.replace('_', ' ').title()
            print(f"{dim_name:<30} {result['score']}/10{'':<4} {result['weight']*100:.0f}%{'':<4} {result['weighted_score']:.2f}")
        
        if scoring_result['strong_dimensions']:
            print("\n" + "-"*80)
            print("STRONG DIMENSIONS (8+):")
            print("-"*80)
            for dim in scoring_result['strong_dimensions']:
                dim_name = dim.replace('_', ' ').title()
                score = scoring_result['dimensions'][dim]['score']
                print(f"  ✓ {dim_name}: {score}/10")
        
        if scoring_result['weak_dimensions']:
            print("\n" + "-"*80)
            print("WEAK DIMENSIONS (<6):")
            print("-"*80)
            for dim in scoring_result['weak_dimensions']:
                dim_name = dim.replace('_', ' ').title()
                score = scoring_result['dimensions'][dim]['score']
                print(f"  ⚠ {dim_name}: {score}/10 - Needs improvement")
        
        print("\n" + "="*80)
    
    def get_improvement_suggestions(self, scoring_result: Dict) -> List[str]:
        """Generate improvement suggestions based on scores."""
        suggestions = []
        
        dimensions = scoring_result['dimensions']
        
        # Content Quality
        if dimensions.get('content_quality', {}).get('score', 0) < 7:
            suggestions.append("Improve content quality: Ensure you're providing unique value, high production quality, and accurate information")
        
        # Title Optimization
        if dimensions.get('title_optimization', {}).get('score', 0) < 7:
            suggestions.append("Optimize title: Include keywords, create curiosity, use power words, keep length 50-60 characters")
        
        # Thumbnail Optimization
        if dimensions.get('thumbnail_optimization', {}).get('score', 0) < 7:
            suggestions.append("Improve thumbnail: Use high contrast colors, readable text, compelling composition, mobile optimization")
        
        # SEO Optimization
        if dimensions.get('seo_optimization', {}).get('score', 0) < 7:
            suggestions.append("Enhance SEO: Write comprehensive description, add relevant tags, include keywords naturally, complete metadata")
        
        # Audience Alignment
        if dimensions.get('audience_alignment', {}).get('score', 0) < 7:
            suggestions.append("Better align with audience: Match expectations, address needs, appropriate difficulty level, relevant topic")
        
        # Engagement Potential
        if dimensions.get('engagement_potential', {}).get('score', 0) < 7:
            suggestions.append("Increase engagement potential: Strengthen hook, add clear CTAs, create interaction opportunities, make shareable")
        
        # Competitive Positioning
        if dimensions.get('competitive_positioning', {}).get('score', 0) < 7:
            suggestions.append("Improve competitive positioning: Differentiate from competitors, clarify unique value, optimize timing, align with trends")
        
        # Production Value
        if dimensions.get('production_value', {}).get('score', 0) < 7:
            suggestions.append("Enhance production value: Improve video/audio quality, polish editing, ensure professional appearance")
        
        return suggestions


def interactive_scoring():
    """Interactive scoring interface."""
    scorer = ContentScorer()
    
    print("\n" + "="*80)
    print("CONTENT SCORING TOOL")
    print("="*80)
    print("\nScore your content across 8 dimensions (1-10 scale)")
    print("10 = Excellent, 5 = Average, 1 = Poor\n")
    
    scores = {}
    
    for dimension, info in scorer.dimensions.items():
        dim_name = dimension.replace('_', ' ').title()
        print(f"\n{dim_name}")
        print(f"  {info['description']}")
        
        while True:
            try:
                score = int(input(f"  Score (1-10): "))
                if 1 <= score <= 10:
                    scores[dimension] = score
                    break
                else:
                    print("  Please enter a score between 1 and 10")
            except ValueError:
                print("  Please enter a valid number")
    
    # Score the content
    result = scorer.score_content(scores)
    
    # Print report
    scorer.print_score_report(result)
    
    # Print suggestions
    suggestions = scorer.get_improvement_suggestions(result)
    if suggestions:
        print("\n" + "-"*80)
        print("IMPROVEMENT SUGGESTIONS")
        print("-"*80)
        for i, suggestion in enumerate(suggestions, 1):
            print(f"\n{i}. {suggestion}")
    
    # Save results
    save = input("\nSave results to file? (y/n): ").lower().strip()
    if save == 'y':
        filename = input("Filename (default: content_score.json): ").strip() or "content_score.json"
        with open(filename, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"✓ Results saved to {filename}")


def main():
    """Main function."""
    interactive_scoring()


if __name__ == '__main__':
    main()

