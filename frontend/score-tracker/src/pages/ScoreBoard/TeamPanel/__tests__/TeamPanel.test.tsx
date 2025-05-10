import { render, screen } from '@testing-library/react';
import TeamPanel from '../TeamPanel';
import { expect, test } from 'vitest';

test('renders without error', () => {
  render(<TeamPanel team='Optic Texas' score={200}/>);
});

test('renders score when passed a negative number', () => {
  render(<TeamPanel team='Atlanta Faze' score={-300}/>);
  const teamElement: HTMLElement = screen.getByText('Atlanta Faze');
  const negScoreElement: HTMLElement = screen.getByText(-300);

  expect(teamElement).toBeVisible();
  expect(negScoreElement).toBeVisible();
});

test('renders score when passed a value of 0', () => {
  render(<TeamPanel team='Atlanta Faze' score={0}/>);
  const teamElement: HTMLElement = screen.getByText('Atlanta Faze');
  const zeroScoreElement: HTMLElement = screen.getByText(0);

  expect(teamElement).toBeVisible();
  expect(zeroScoreElement).toBeVisible();
});

test('renders for the team scores when score prop is null', () => {
  render(<TeamPanel team='Vegas Faclons' score={null}/>);
  const scoreElement: HTMLElement = screen.getByText('--');

  expect(scoreElement).toBeVisible();
});