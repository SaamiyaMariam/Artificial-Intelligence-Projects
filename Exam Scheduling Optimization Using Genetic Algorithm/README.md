# Exam Schedule Optimization using Genetic Algorithm

This project implements a Genetic Algorithm to optimize exam schedules based on various constraints such as time slots, exam halls, and potential conflicts between exams.

## Overview

The exam schedule optimization is approached as a genetic algorithm problem, with the goal of finding the best schedule that minimizes conflicts and maximizes efficient hall usage.

## Project Structure

- `main.py`: The main script that contains the genetic algorithm implementation for exam schedule optimization.

## Configuration

The configuration parameters in `main.py` include:
- `max_hours`: Maximum hours an exam hall can be occupied in a day.
- `pop_size`: Population size, representing the number of schedules in each generation.
- `num_courses`: Number of courses for which exams need to be scheduled.
- `num_time_slots`: Number of available time slots for exams in a day.
- `num_halls`: Number of exam halls available.
- `num_conflicts`: Number of predefined exam conflicts.
- `overtime_penalty`: Penalty for exceeding the maximum hall occupancy hours.
- `confliction_penalty`: Penalty for exam conflicts.
- `fitness_values`: List to store the fitness values of schedules.
- `schedule_population`: List to store multiple schedules representing the population.
- `num_gens`: Number of generations for the genetic algorithm.

## Usage

1. Adjust the configuration parameters in `main.py` based on your requirements.
2. Run the script:
   ```bash
   python main.py
    ```
The algorithm will run for a specified number of generations, and the best schedule with the highest fitness value will be displayed.
