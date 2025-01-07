"""
Training Program Data Management System
------------------------------------
This system manages and analyzes data for a 4-month training program on digital literacy, AI, and robotics.
It generates dummy data, processes it, creates visualizations, and generates reports.

Example Usage:
    # Initialize and run the system
    data_generator = TrainingDataGenerator()
    data = data_generator.generate_dummy_data()
    
    # Create management system
    tms = TrainingManagementSystem(data)
    
    # Generate visualizations and reports
    tms.generate_visualizations()
    report = tms.generate_comprehensive_report()
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
import numpy as np
from pathlib import Path

class TrainingDataGenerator:
    """
    Generates dummy training data for demonstration purposes.
    
    Example data point:
    {
        'date': '2024-01-01',
        'girls_attendance': 20,
        'boys_attendance': 22,
        'total_attendance': 42,
        'girls_engagement': 4.2,
        'boys_engagement': 4.1,
        'material_effectiveness': 4.5,
        'teaching_effectiveness': 4.3,
        'trainer_attendance': 1,
        'daily_assessment_score': 75.5,
        'practical_skills_score': 82.3,
        'theoretical_knowledge': 78.9,
        'project_completion_rate': 85.5,
        'participation_rate': 90.0,
        'homework_completion': 88.5
    }
    """
    
    def __init__(self, start_date=datetime(2024, 1, 1), num_days=120):
        """
        Initialize the data generator.
        
        Args:
            start_date: Starting date for the training program (default: Jan 1, 2024)
            num_days: Duration of the program in days (default: 120 days = 4 months)
        """
        self.start_date = start_date
        self.num_days = num_days
        
    def generate_dummy_data(self):
        """
        Generates dummy data for the entire training period.
        
        Returns:
            pandas.DataFrame: Contains daily training metrics
            
        Example:
            generator = TrainingDataGenerator()
            data = generator.generate_dummy_data()
            print(data.head())  # View first 5 days of data
        """
        data = []
        for day in range(self.num_days):
            current_date = self.start_date + timedelta(days=day)
            # Skip weekends (Saturday=5, Sunday=6)
            if current_date.weekday() >= 5:
                continue
                
            # Generate random attendance (15-25 students per gender)
            num_girls = random.randint(15, 25)
            num_boys = random.randint(15, 25)
            
            # Generate baseline and progressive assessment scores
            # First day scores start lower (50-65) and gradually improve
            if day == 0:  # First day - baseline
                self.baseline_score = random.uniform(50, 65)
            # Progressive improvement over time with some randomness
            current_score = min(95, self.baseline_score + (day/self.num_days) * random.uniform(20, 30))
            
            # Create daily data point with all metrics
            data.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'girls_attendance': num_girls,
                'boys_attendance': num_boys,
                'total_attendance': num_girls + num_boys,
                'girls_engagement': random.uniform(3.5, 5.0),  # Engagement scale: 3.5-5.0
                'boys_engagement': random.uniform(3.5, 5.0),
                'material_effectiveness': random.uniform(3.0, 5.0),  # Effectiveness scale: 3.0-5.0
                'teaching_effectiveness': random.uniform(3.5, 5.0),
                'trainer_attendance': random.choice([0, 1]),  # 0=absent, 1=present
                'daily_assessment_score': current_score,  # Progressive improvement
                'practical_skills_score': random.uniform(60, 95),
                'theoretical_knowledge': random.uniform(60, 95),
                'project_completion_rate': random.uniform(70, 100),
                'participation_rate': random.uniform(75, 100),
                'homework_completion': random.uniform(70, 100)
            })
        
        return pd.DataFrame(data)

class TrainingManagementSystem:
    """
    Manages training data analysis and visualization.
    
    Example:
        data = pd.DataFrame(...)  # Your training data
        tms = TrainingManagementSystem(data)
        tms.generate_visualizations()
        report = tms.generate_comprehensive_report()
    """
    
    def __init__(self, data):
        """
        Initialize the management system with training data.
        
        Args:
            data (pandas.DataFrame): Training program data
        """
        self.data = data
        self.output_dir = Path('output')
        self.output_dir.mkdir(exist_ok=True)
    
    def get_attendance_metrics(self):
        """
        Calculate attendance-related metrics.
        
        Returns:
            dict: Contains average attendance and engagement metrics
            
        Example:
            metrics = tms.get_attendance_metrics()
            print(f"Average total attendance: {metrics['avg_total_attendance']:.2f}")
        """
        metrics = {
            'avg_total_attendance': self.data['total_attendance'].mean(),
            'avg_girls_attendance': self.data['girls_attendance'].mean(),
            'avg_boys_attendance': self.data['boys_attendance'].mean(),
            'avg_girls_engagement': self.data['girls_engagement'].mean(),
            'avg_boys_engagement': self.data['boys_engagement'].mean(),
            'attendance_trend': self.data['total_attendance'].pct_change().mean() * 100
        }
        return metrics
    
    def get_performance_metrics(self):
        """
        Calculate performance-related metrics.
        
        Returns:
            dict: Contains various performance and effectiveness metrics
            
        Example:
            metrics = tms.get_performance_metrics()
            print(f"Average assessment score: {metrics['avg_daily_assessment']:.2f}%")
        """
        metrics = {
            'avg_material_effectiveness': self.data['material_effectiveness'].mean(),
            'avg_teaching_effectiveness': self.data['teaching_effectiveness'].mean(),
            'avg_daily_assessment': self.data['daily_assessment_score'].mean(),
            'trainer_attendance_rate': (self.data['trainer_attendance'].sum() / len(self.data)) * 100,
            'avg_practical_skills': self.data['practical_skills_score'].mean(),
            'avg_theoretical_knowledge': self.data['theoretical_knowledge'].mean(),
            'avg_project_completion': self.data['project_completion_rate'].mean(),
            'avg_participation': self.data['participation_rate'].mean(),
            'avg_homework_completion': self.data['homework_completion'].mean()
        }
        return metrics
    
    def calculate_impact_assessment(self):
        """
        Calculate the impact of the training program by comparing baseline and endline metrics.
        
        Returns:
            dict: Contains improvement metrics and overall impact
            
        Example:
            impact = tms.calculate_impact_assessment()
            print(f"Overall improvement: {impact['overall_improvement_percentage']:.2f}%")
        """
        baseline = self.data.iloc[0]  # First day metrics
        endline = self.data.iloc[-1]  # Last day metrics
        
        impact = {
            'assessment_improvement': endline['daily_assessment_score'] - baseline['daily_assessment_score'],
            'practical_skills_improvement': endline['practical_skills_score'] - baseline['practical_skills_score'],
            'theoretical_knowledge_improvement': endline['theoretical_knowledge'] - baseline['theoretical_knowledge'],
            'overall_improvement_percentage': ((endline['daily_assessment_score'] / baseline['daily_assessment_score']) - 1) * 100
        }
        return impact
    
    def generate_visualizations(self):
        """
        Generate a comprehensive dashboard with multiple visualizations.
        
        Creates a dashboard.png file with 5 subplots:
        1. Attendance trends
        2. Performance distribution
        3. Gender engagement
        4. Material effectiveness
        5. Completion rates
        
        Example:
            tms.generate_visualizations()
            # Check output/dashboard.png for the result
        """
        # Create a dashboard layout
        plt.style.use('default')
        fig = plt.figure(figsize=(15, 12), facecolor='white')
        
        # Define grid layout with more space
        gs = plt.GridSpec(3, 2, figure=fig, hspace=0.6, wspace=0.3, 
                         top=0.95, bottom=0.08, left=0.1, right=0.9)
        
        fig.suptitle('Training Program Analytics Dashboard', fontsize=16, y=0.98)
        
        # Convert dates once
        dates = pd.to_datetime(self.data['date'])
        
        # 1. Weekly Revenue Chart (Attendance Trends) - Larger plot
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(range(len(dates)), self.data['girls_attendance'], 
                label='Girls', color='#FFA500', linewidth=2)
        ax1.plot(range(len(dates)), self.data['boys_attendance'], 
                label='Boys', color='#4B0082', linewidth=2)
        ax1.set_title('Weekly Attendance Trends', pad=20)
        ax1.set_xlabel('Date', labelpad=10)
        ax1.set_ylabel('Number of Students', labelpad=10)
        
        # Set x-axis ticks and labels
        num_dates = len(dates)
        step = num_dates // 6  # Show only 6 dates
        tick_positions = range(0, num_dates, step)
        tick_labels = [dates[i].strftime('%Y-%m-%d') for i in tick_positions]
        ax1.set_xticks(tick_positions)
        ax1.set_xticklabels(tick_labels, rotation=30, ha='right')
        
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.legend()
        
        # 2. Performance Distribution
        ax2 = fig.add_subplot(gs[1, 0])
        performance_data = [
            self.data['daily_assessment_score'].mean(),
            self.data['practical_skills_score'].mean(),
            self.data['theoretical_knowledge'].mean()
        ]
        labels = ['Assessment', 'Practical', 'Theory']
        colors = ['#FFA500', '#4B0082', '#228B22']
        bars = ax2.bar(labels, performance_data, color=colors)
        ax2.set_title('Performance Distribution', pad=20)
        ax2.set_ylabel('Average Score', labelpad=10)
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom')
        ax2.grid(True, linestyle='--', alpha=0.7, axis='y')
        
        # 3. Engagement by Gender
        ax3 = fig.add_subplot(gs[1, 1])
        engagement_data = {
            'Girls': self.data['girls_engagement'].mean(),
            'Boys': self.data['boys_engagement'].mean()
        }
        bars = ax3.bar(engagement_data.keys(), engagement_data.values(), 
                color=['#FFA500', '#4B0082'])
        ax3.set_title('Engagement by Gender', pad=20)
        ax3.set_ylabel('Engagement Score (out of 5)', labelpad=10)
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom')
        ax3.grid(True, linestyle='--', alpha=0.7, axis='y')
        
        # 4. Material Effectiveness Over Time
        ax4 = fig.add_subplot(gs[2, 0])
        ax4.plot(range(len(dates)), self.data['material_effectiveness'], 
                color='#228B22', linewidth=2)
        ax4.set_title('Material Effectiveness Trend', pad=20)
        ax4.set_xlabel('Date', labelpad=10)
        ax4.set_ylabel('Effectiveness Score', labelpad=10)
        
        # Set x-axis ticks and labels (same as ax1)
        ax4.set_xticks(tick_positions)
        ax4.set_xticklabels(tick_labels, rotation=30, ha='right')
        
        ax4.grid(True, linestyle='--', alpha=0.7)
        
        # 5. Project Completion Rates
        ax5 = fig.add_subplot(gs[2, 1])
        completion_data = [
            self.data['project_completion_rate'].mean(),
            self.data['homework_completion'].mean(),
            self.data['participation_rate'].mean()
        ]
        labels = ['Projects', 'Homework', 'Participation']
        bars = ax5.bar(labels, completion_data, color=['#4B0082', '#FFA500', '#228B22'])
        ax5.set_title('Completion Rates', pad=20)
        ax5.set_ylabel('Completion Rate (%)', labelpad=10)
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax5.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom')
        ax5.grid(True, linestyle='--', alpha=0.7, axis='y')
        
        # Save figure
        plt.savefig(self.output_dir / 'dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
    
    def generate_comprehensive_report(self):
        """
        Generate a detailed report of all metrics and assessments.
        
        Returns:
            str: Formatted report text
            
        Example:
            report = tms.generate_comprehensive_report()
            with open('report.txt', 'w') as f:
                f.write(report)
        """
        attendance_metrics = self.get_attendance_metrics()
        performance_metrics = self.get_performance_metrics()
        impact_assessment = self.calculate_impact_assessment()
        
        report = "Training Program Comprehensive Analysis Report\n"
        report += "=" * 50 + "\n\n"
        
        report += "1. Attendance Metrics\n"
        report += "-" * 20 + "\n"
        report += f"• Average Total Attendance: {attendance_metrics['avg_total_attendance']:.2f}\n"
        report += f"• Average Girls Attendance: {attendance_metrics['avg_girls_attendance']:.2f}\n"
        report += f"• Average Boys Attendance: {attendance_metrics['avg_boys_attendance']:.2f}\n"
        report += f"• Attendance Trend: {attendance_metrics['attendance_trend']:.2f}% change\n\n"
        
        report += "2. Engagement Metrics\n"
        report += "-" * 20 + "\n"
        report += f"• Girls Engagement: {attendance_metrics['avg_girls_engagement']:.2f}/5.0\n"
        report += f"• Boys Engagement: {attendance_metrics['avg_boys_engagement']:.2f}/5.0\n\n"
        
        report += "3. Performance Metrics\n"
        report += "-" * 20 + "\n"
        report += f"• Material Effectiveness: {performance_metrics['avg_material_effectiveness']:.2f}/5.0\n"
        report += f"• Teaching Effectiveness: {performance_metrics['avg_teaching_effectiveness']:.2f}/5.0\n"
        report += f"• Average Assessment Score: {performance_metrics['avg_daily_assessment']:.2f}%\n"
        report += f"• Practical Skills Score: {performance_metrics['avg_practical_skills']:.2f}%\n"
        report += f"• Theoretical Knowledge: {performance_metrics['avg_theoretical_knowledge']:.2f}%\n"
        report += f"• Project Completion Rate: {performance_metrics['avg_project_completion']:.2f}%\n"
        report += f"• Participation Rate: {performance_metrics['avg_participation']:.2f}%\n"
        report += f"• Homework Completion: {performance_metrics['avg_homework_completion']:.2f}%\n\n"
        
        report += "4. Impact Assessment\n"
        report += "-" * 20 + "\n"
        report += f"• Assessment Score Improvement: {impact_assessment['assessment_improvement']:.2f} points\n"
        report += f"• Practical Skills Improvement: {impact_assessment['practical_skills_improvement']:.2f} points\n"
        report += f"• Theoretical Knowledge Improvement: {impact_assessment['theoretical_knowledge_improvement']:.2f} points\n"
        report += f"• Overall Improvement: {impact_assessment['overall_improvement_percentage']:.2f}%\n"
        
        return report

def main():
    """
    Main function to run the training management system.
    
    Example:
        python training_management.py
    """
    # Generate dummy data
    data_generator = TrainingDataGenerator()
    data = data_generator.generate_dummy_data()
    
    # Save raw data
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    data.to_csv(output_dir / 'training_data.csv', index=False)
    
    # Initialize system and generate reports
    tms = TrainingManagementSystem(data)
    
    # Generate dashboard and reports
    tms.generate_visualizations()
    
    # Generate and save comprehensive report
    report = tms.generate_comprehensive_report()
    with open(output_dir / 'comprehensive_report.txt', 'w') as f:
        f.write(report)
    
    print("Data management system has processed the information.")
    print("Check the 'output' directory for:")
    print("1. training_data.csv - Raw data")
    print("2. dashboard.png - Analytics Dashboard")
    print("3. comprehensive_report.txt - Detailed analysis report")

if __name__ == "__main__":
    main() 