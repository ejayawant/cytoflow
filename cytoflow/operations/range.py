from cytoflow import Experiment
from traits.api import HasTraits, CFloat, Str, CStr
import pandas as pd
from traits.has_traits import provides
from cytoflow.operations.i_operation import IOperation

@provides(IOperation)
class RangeOp(HasTraits):
    """Apply a range gate to a cytometry experiment.
    
    Attributes
    ----------
    name : Str
        The operation name.  Used to name the new metadata field in the
        experiment that's created by apply()
        
    channel : Str
        The name of the channel to apply the range gate.
        
    low : Float
        The lowest value to include in this gate.
        
    high : Float
        The highest value to include in this gate.
    """
    
    # traits
    id = "edu.mit.synbio.cytoflow.operations.range"
    friendly_id = "Range"
    
    name = CStr()
    channel = Str()
    low = CFloat()
    high = CFloat()
    
    def is_valid(self, experiment):
        """Validate this operation against an experiment."""

        if not self.name:
            return False
        
        if self.name in self.experiment.columns:
            return False
        
        if not self.channel:
            return False
        
        if not self.channel in experiment.channels:
            return False
        
        if self.high <= self.low:
            return False
        
        if self.high <= experiment[self.channel].min() or \
           self.low >= experiment[self.channel].max:
            return False
       
        return True
        
    def apply(self, old_experiment):
        """Applies the threshold to an experiment.
        
        Parameters
        ----------
        experiment : Experiment
            the old_experiment to which this op is applied
            
        Returns
        -------
            a new experiment, the same as old_experiment but with a new
            column the same as the operation name.  The bool is True if the
            event's measurement in self.channel is greater than self.low and
            less than self.high; it is False otherwise.
        """
        
        # make sure name got set!
        if not self.name:
            raise RuntimeError("You have to set the Threshold gate's name "
                               "before applying it!")
        
        # make sure old_experiment doesn't already have a column named self.name
        if(self.name in old_experiment.data.columns):
            raise RuntimeError("Experiment already contains a column {0}"
                               .format(self.name))
        
        new_experiment = old_experiment.clone()
        new_experiment[self.name] = \
            new_experiment[self.channel].between(self.low, self.high)
            
        new_experiment.conditions[self.name] = "bool"
        new_experiment.metadata[self.name] = {}
            
        return new_experiment
    
    def default_view(self, experiment):
        """Returns a histogram view with the threshold highlighted."""
        raise NotImplementedError
    