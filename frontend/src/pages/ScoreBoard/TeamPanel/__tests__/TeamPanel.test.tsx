import { render, screen } from '@testing-library/react';
import TeamPanel from '../TeamPanel';
import { expect, describe, it } from 'vitest';

describe('TeamPanel', () => {
  it('renders without error', () => {
    render(<TeamPanel team='optic' score={250}/>);
    const imgElement = screen.getByRole('img', { name: 'optic' });
    const scoreElement = screen.getByText(250);
    expect(imgElement).toBeInTheDocument();
    expect(scoreElement).toBeInTheDocument();
  });
});