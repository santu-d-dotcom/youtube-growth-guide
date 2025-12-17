"""
Content Performance Analyzer
Analyzes YouTube channel content performance to identify patterns and opportunities.

Usage:
    python content_performance_analyzer.py
"""

import json
import csv
from collections import defaultdict
from typing import Dict, List, Tuple
from datetime import datetime


class ContentPerformanceAnalyzer:
    """Analyzes content performance data to identify patterns."""
    
    def __init__(self):
        self.content_data = []
        self.analysis_results = {}
    
    def load_data_from_csv(self, csv_file: str):
        """Load content data from CSV file.
        
        Expected CSV format:
        title,content_type,topic,views,watch_time,likes,comments,subscribers_gained,upload_date
        """
        self.content_data = []
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert numeric fields
                    row['views'] = int(row.get('views', 0))
                    row['watch_time'] = float(row.get('watch_time', 0))
                    row['likes'] = int(row.get('likes', 0))
                    row['comments'] = int(row.get('comments', 0))
                    row['subscribers_gained'] = int(row.get('subscribers_gained', 0))
                    self.content_data.append(row)
            print(f"✓ Loaded {len(self.content_data)} videos from {csv_file}")
        except FileNotFoundError:
            print(f"✗ Error: File {csv_file} not found")
            print("Creating sample template...")
            self.create_sample_template(csv_file)
    
    def create_sample_template(self, csv_file: str):
        """Create a sample CSV template."""
        sample_data = [
            {
                'title': 'Sample Video 1',
                'content_type': 'Tutorial',
                'topic': 'Python Basics',
                'views': 1000,
                'watch_time': 500,
                'likes': 50,
                'comments': 10,
                'subscribers_gained': 20,
                'upload_date': '2024-01-01'
            }
        ]
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            if sample_data:
                writer = csv.DictWriter(f, fieldnames=sample_data[0].keys())
                writer.writeheader()
                writer.writerows(sample_data)
        
        print(f"✓ Created sample template: {csv_file}")
        print("Please fill in your actual data and run again.")
    
    def analyze_by_content_type(self) -> Dict:
        """Analyze performance by content type."""
        type_stats = defaultdict(lambda: {
            'count': 0,
            'total_views': 0,
            'total_watch_time': 0,
            'total_likes': 0,
            'total_comments': 0,
            'total_subscribers': 0
        })
        
        for video in self.content_data:
            content_type = video.get('content_type', 'Unknown')
            type_stats[content_type]['count'] += 1
            type_stats[content_type]['total_views'] += video.get('views', 0)
            type_stats[content_type]['total_watch_time'] += video.get('watch_time', 0)
            type_stats[content_type]['total_likes'] += video.get('likes', 0)
            type_stats[content_type]['total_comments'] += video.get('comments', 0)
            type_stats[content_type]['total_subscribers'] += video.get('subscribers_gained', 0)
        
        # Calculate averages
        results = {}
        for content_type, stats in type_stats.items():
            count = stats['count']
            if count > 0:
                results[content_type] = {
                    'video_count': count,
                    'avg_views': stats['total_views'] / count,
                    'avg_watch_time': stats['total_watch_time'] / count,
                    'avg_likes': stats['total_likes'] / count,
                    'avg_comments': stats['total_comments'] / count,
                    'avg_subscribers': stats['total_subscribers'] / count,
                    'engagement_rate': (stats['total_likes'] + stats['total_comments']) / stats['total_views'] * 100 if stats['total_views'] > 0 else 0
                }
        
        return results
    
    def analyze_by_topic(self) -> Dict:
        """Analyze performance by topic."""
        topic_stats = defaultdict(lambda: {
            'count': 0,
            'total_views': 0,
            'total_watch_time': 0,
            'total_likes': 0,
            'total_comments': 0,
            'total_subscribers': 0
        })
        
        for video in self.content_data:
            topic = video.get('topic', 'Unknown')
            topic_stats[topic]['count'] += 1
            topic_stats[topic]['total_views'] += video.get('views', 0)
            topic_stats[topic]['total_watch_time'] += video.get('watch_time', 0)
            topic_stats[topic]['total_likes'] += video.get('likes', 0)
            topic_stats[topic]['total_comments'] += video.get('comments', 0)
            topic_stats[topic]['total_subscribers'] += video.get('subscribers_gained', 0)
        
        # Calculate averages
        results = {}
        for topic, stats in topic_stats.items():
            count = stats['count']
            if count > 0:
                results[topic] = {
                    'video_count': count,
                    'avg_views': stats['total_views'] / count,
                    'avg_watch_time': stats['total_watch_time'] / count,
                    'avg_likes': stats['total_likes'] / count,
                    'avg_comments': stats['total_comments'] / count,
                    'avg_subscribers': stats['total_subscribers'] / count,
                    'engagement_rate': (stats['total_likes'] + stats['total_comments']) / stats['total_views'] * 100 if stats['total_views'] > 0 else 0
                }
        
        return results
    
    def identify_top_performers(self, metric: str = 'views', top_n: int = 10) -> List[Dict]:
        """Identify top performing videos by metric."""
        sorted_videos = sorted(
            self.content_data,
            key=lambda x: x.get(metric, 0),
            reverse=True
        )
        return sorted_videos[:top_n]
    
    def identify_underperformers(self, metric: str = 'views', bottom_n: int = 10) -> List[Dict]:
        """Identify underperforming videos by metric."""
        sorted_videos = sorted(
            self.content_data,
            key=lambda x: x.get(metric, 0)
        )
        return sorted_videos[:bottom_n]
    
    def calculate_engagement_rate(self, video: Dict) -> float:
        """Calculate engagement rate for a video."""
        views = video.get('views', 0)
        if views == 0:
            return 0.0
        likes = video.get('likes', 0)
        comments = video.get('comments', 0)
        return ((likes + comments) / views) * 100
    
    def generate_recommendations(self) -> List[str]:
        """Generate actionable recommendations based on analysis."""
        recommendations = []
        
        # Analyze content types
        type_analysis = self.analyze_by_content_type()
        if type_analysis:
            best_type = max(type_analysis.items(), key=lambda x: x[1]['avg_views'])
            worst_type = min(type_analysis.items(), key=lambda x: x[1]['avg_views'])
            
            recommendations.append(
                f"✓ Double down on '{best_type[0]}' content (avg {best_type[1]['avg_views']:.0f} views)"
            )
            recommendations.append(
                f"⚠ Review '{worst_type[0]}' content strategy (avg {worst_type[1]['avg_views']:.0f} views)"
            )
        
        # Analyze topics
        topic_analysis = self.analyze_by_topic()
        if topic_analysis:
            best_topic = max(topic_analysis.items(), key=lambda x: x[1]['avg_views'])
            recommendations.append(
                f"✓ Create more content on '{best_topic[0]}' topic (avg {best_topic[1]['avg_views']:.0f} views)"
            )
        
        # Top performers
        top_videos = self.identify_top_performers('views', 5)
        if top_videos:
            recommendations.append(
                f"✓ Study top performer: '{top_videos[0].get('title', 'N/A')}' ({top_videos[0].get('views', 0)} views)"
            )
        
        return recommendations
    
    def print_analysis_report(self):
        """Print comprehensive analysis report."""
        print("\n" + "="*80)
        print("CONTENT PERFORMANCE ANALYSIS REPORT")
        print("="*80)
        
        if not self.content_data:
            print("\n⚠ No data loaded. Please load data first.")
            return
        
        print(f"\nTotal Videos Analyzed: {len(self.content_data)}")
        
        # Content Type Analysis
        print("\n" + "-"*80)
        print("PERFORMANCE BY CONTENT TYPE")
        print("-"*80)
        type_analysis = self.analyze_by_content_type()
        if type_analysis:
            print(f"\n{'Content Type':<20} {'Videos':<10} {'Avg Views':<15} {'Engagement %':<15}")
            print("-"*80)
            for content_type, stats in sorted(type_analysis.items(), key=lambda x: x[1]['avg_views'], reverse=True):
                print(f"{content_type:<20} {stats['video_count']:<10} {stats['avg_views']:<15.0f} {stats['engagement_rate']:<15.2f}")
        
        # Topic Analysis
        print("\n" + "-"*80)
        print("PERFORMANCE BY TOPIC")
        print("-"*80)
        topic_analysis = self.analyze_by_topic()
        if topic_analysis:
            print(f"\n{'Topic':<30} {'Videos':<10} {'Avg Views':<15} {'Engagement %':<15}")
            print("-"*80)
            for topic, stats in sorted(topic_analysis.items(), key=lambda x: x[1]['avg_views'], reverse=True):
                print(f"{topic:<30} {stats['video_count']:<10} {stats['avg_views']:<15.0f} {stats['engagement_rate']:<15.2f}")
        
        # Top Performers
        print("\n" + "-"*80)
        print("TOP 10 PERFORMING VIDEOS (by views)")
        print("-"*80)
        top_videos = self.identify_top_performers('views', 10)
        print(f"\n{'Title':<40} {'Views':<15} {'Engagement %':<15}")
        print("-"*80)
        for video in top_videos:
            engagement = self.calculate_engagement_rate(video)
            title = video.get('title', 'N/A')[:40]
            print(f"{title:<40} {video.get('views', 0):<15} {engagement:<15.2f}")
        
        # Recommendations
        print("\n" + "-"*80)
        print("RECOMMENDATIONS")
        print("-"*80)
        recommendations = self.generate_recommendations()
        for rec in recommendations:
            print(f"\n{rec}")
        
        print("\n" + "="*80)


def main():
    """Main function to run the analyzer."""
    analyzer = ContentPerformanceAnalyzer()
    
    # Try to load data
    csv_file = 'content_data.csv'
    analyzer.load_data_from_csv(csv_file)
    
    # Generate report
    analyzer.print_analysis_report()
    
    # Save results to JSON
    results = {
        'content_type_analysis': analyzer.analyze_by_content_type(),
        'topic_analysis': analyzer.analyze_by_topic(),
        'top_performers': [
            {k: v for k, v in video.items() if k != 'upload_date'}
            for video in analyzer.identify_top_performers('views', 10)
        ],
        'recommendations': analyzer.generate_recommendations()
    }
    
    with open('analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print("\n✓ Analysis results saved to analysis_results.json")


if __name__ == '__main__':
    main()

