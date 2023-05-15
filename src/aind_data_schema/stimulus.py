""" schema for session stimulus """

from __future__ import annotations

from datetime import time
from enum import Enum
from typing import Any, Dict, Optional, Union, List

from pydantic import Field

from .base import AindModel
from .device import FrequencyUnit
from .procedures import TimeUnit


class PulseShape(Enum):
    """Types of Opto stim pulse shapes"""

    SQUARE = "Square"
    RAMP = "Ramp"
    SINE = "Sinusoidal"


class OptoStim(AindModel):
    """Description of opto stimulation parameters"""

    stimulus_name: str = Field(..., title="Stimulus name")
    pulse_shape: PulseShape = Field(..., title="Pulse shape")
    pulse_frequency: int = Field(..., title="Pulse frequency (Hz)")
    pulse_frequency_unit: FrequencyUnit = Field(FrequencyUnit.HZ, title="Pulse frequency unit")
    number_pulse_trains: int = Field(..., title="Number of pulse trains")
    pulse_width: int = Field(..., title="Pulse width (ms)")
    pulse_width_unit: TimeUnit = Field(TimeUnit.MS, title="Pulse width unit")
    pulse_train_duration: float = Field(..., title="Pulse train duration (s)")
    pulse_train_duration_unit: TimeUnit = Field(TimeUnit.S, title="Pulse train duration unit")
    fixed_pulse_train_interval: bool = Field(..., title="Fixed pulse train interval")
    pulse_train_interval: Optional[float] = Field(None, title="Pulse train interval (s)", description="Time between pulse trains")
    pulse_train_interval_unit: TimeUnit = Field(TimeUnit.S, title="Pulse train interval unit")
    baseline_duration: float = Field(
        ..., title="Baseline duration (s)", description="Duration of baseline recording prior to first pulse train"
    )
    baseline_duration_unit: TimeUnit = Field(TimeUnit.S, title="Baseline duration unit")
    other_parameters: Optional[Dict[str, Any]]
    notes: Optional[str] = Field(None, title="Notes")


class VisualStim(AindModel):
    """Description of visual stimulus parameters. Provides a high level description of stimulus."""

    stimulus_name: str = Field(..., title="Stimulus name")
    number_of_conditions: int = Field(
        ..., 
        title="Number of conditions",
        description="Number of unique stimulus conditions",
    )
    stimulus_parameters: Optional[Dict[str, Any]] = Field(
        None, 
        title="Stimulus parameters",
        description="Define and list the parameter values used (e.g. all TF or orientation values)"
    )
    stimulus_template_name: Optional[List[str]] = Field(
        None,
        title="Stimulus template name",
        description="Name of image set or movie displayed"
    )
    trial_duration: float = Field(..., title="Trial duration (s)")
    trial_duration_unit: TimeUnit = Field(TimeUnit.S, title="Trial duration unit")
    inter_trial_interval: float = Field(..., title="Inter trial interval (s)")
    inter_trial_interval_unit: TimeUnit = Field(TimeUnit.S, title="Inter trial interval unit")
    number_of_trials: int = Field(
        ...,
        title="Number of trials",
        description="Number of trials per condition"
    )
    stimulus_software: Optional[str] = Field(
        ..., 
        title="Stimulus software",
        description="The software used to control the stimulus (e.g. Bonsai)",
    )
    stimulus_software_version: Optional[str] = Field(..., title="Stimulus software version")
    stimulus_script: Optional[str] = Field(
        ..., 
        title="Stimulus script",
        description="The specific code for this stimulus instance",
    )
    stimulus_script_version: Optional[str] = Field(..., "Stimulus srcipt version")
    notes: Optional[str] = Field(None, title="Notes")


class StimulusPresentation(AindModel):
    """Description of stimulus used during session"""

    stimulus: Union[OptoStim, VisualStim] = Field(..., title="Stimulus")
    stimulus_start_time: time = Field(
        ...,
        title="Stimulus start time",
        description="When a specific stimulus begins. This might be the same as the session start time.",
    )
    stimulus_end_time: time = Field(
        ...,
        title="Stimulus end time",
        description="When a specific stimulus ends. This might be the same as the session end time.",
    )
