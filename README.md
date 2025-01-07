# Training Program Data Management System

A simple data management system for monitoring a 4-month training program on digital literacy, AI, and robotics for students from grades 6th to 12th.

## Features

- Daily attendance tracking for students (gender-wise) and trainers
- Engagement impact monitoring
- Material effectiveness evaluation
- Performance monitoring
- Teaching methodology assessment
- Automated report generation
- Visual analytics

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the system:
```bash
python training_management.py
```

## Output Files

The system generates three main outputs:

1. `training_data.csv` - Raw data containing all metrics
2. `attendance_trend.png` - Visualization of attendance trends
3. `training_report.txt` - Comprehensive analysis report

## Data Structure

The system tracks the following metrics:
- Daily attendance (girls/boys)
- Student engagement levels
- Material effectiveness
- Teaching effectiveness
- Trainer attendance
- Daily assessment scores

## Note

This version uses dummy data for demonstration. For actual implementation, replace the `generate_dummy_data()` function with real data input mechanisms. 