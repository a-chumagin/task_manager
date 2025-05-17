import { render, screen } from '@testing-library/react';
import Home from '../pages/index';

describe('Home page', () => {
  it('renders header', () => {
    render(<Home />);
    expect(screen.getByText('Task Manager')).toBeInTheDocument();
  });
});
