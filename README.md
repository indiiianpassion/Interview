# Training Program Data Management System

A comprehensive data management system for monitoring a 4-month training program on digital literacy, AI, and robotics for students from grades 6th to 12th.

## System Architecture

The system is built with two main classes:

### 1. TrainingDataGenerator
Handles data generation and simulation:
- Generates 4 months of daily data (excluding weekends)
- Creates baseline and progressive assessment scores
- Simulates attendance, engagement, and performance metrics

Key metrics generated:
- Attendance (15-25 students per gender)
- Engagement scores (3.5-5.0 scale)
- Material/Teaching effectiveness (3.0-5.0 scale)
- Assessment scores (starting 50-65, progressing to max 95)
- Practical and theoretical knowledge (60-95 range)
- Completion rates (70-100%)

### 2. TrainingManagementSystem
Manages data analysis and visualization:

#### Analytics Components:
1. **Attendance Metrics**
   - Average attendance (total and gender-wise)
   - Gender-specific engagement levels
   - Attendance trends over time

2. **Performance Metrics**
   - Material effectiveness
   - Teaching methodology assessment
   - Daily assessment scores
   - Practical and theoretical knowledge levels
   - Project, homework, and participation rates

3. **Impact Assessment**
   - Baseline vs endline comparison
   - Improvement measurements
   - Overall progress percentage

#### Visualization Dashboard
The system generates a comprehensive dashboard with 5 key visualizations:
1. **Weekly Attendance Trends** (Top panel)
   - Gender-wise attendance tracking
   - Time series visualization

2. **Performance Distribution** (Middle-left)
   - Assessment scores
   - Practical skills
   - Theoretical knowledge

3. **Engagement by Gender** (Middle-right)
   - Comparative engagement levels
   - Gender-specific analysis

4. **Material Effectiveness** (Bottom-left)
   - Effectiveness trends over time
   - Teaching methodology impact

5. **Completion Rates** (Bottom-right)
   - Project completion
   - Homework submission
   - Class participation

## Setup and Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- pandas (2.1.4): Data manipulation and analysis
- matplotlib (3.8.2): Visualization and plotting
- seaborn (0.13.0): Enhanced visualizations
- numpy (1.24.3): Numerical computations

2. Run the system:
```bash
python training_management.py
```

## Output Files

The system generates three files in the 'output' directory:

1. `training_data.csv`
   - Raw data with all daily metrics
   - Complete record of attendance, performance, and engagement

2. `dashboard.png`
   - Combined visualization dashboard
   - High-resolution (300 DPI) analytics visualization
   - Five key metric visualizations

3. `comprehensive_report.txt`
   - Detailed analysis report
   - Section-wise metrics breakdown
   - Impact assessment results

## Data Structure

### Input Metrics:
- Daily attendance (girls/boys)
- Student engagement levels (3.5-5.0)
- Material effectiveness (3.0-5.0)
- Teaching effectiveness (3.5-5.0)
- Trainer attendance (binary: 0/1)
- Assessment scores (progressive: 50-95)
- Practical skills (60-95)
- Theoretical knowledge (60-95)
- Completion rates (70-100%)

### Output Analytics:
- Average attendance metrics
- Engagement analysis
- Performance trends
- Impact assessment
- Progress evaluation

## Customization

For real implementation:
1. Replace `generate_dummy_data()` with actual data input
2. Modify assessment ranges in `TrainingDataGenerator`
3. Adjust visualization parameters in `generate_visualizations()`
4. Customize report format in `generate_comprehensive_report()`

## Note

This version uses simulated data for demonstration. For actual deployment:
- Implement data collection mechanisms
- Adjust metric ranges based on actual requirements
- Modify visualization layout as needed
- Add data validation and error handling 