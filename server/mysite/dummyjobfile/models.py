from django.db import models

class DummyTest(models.Model):
    specific_test = models.CharField(max_length=30, default="some test", unique=True, help_text="The specific test name of the test")
    uri = models.CharField(max_length=300, help_text="The URI of the test, should be able to grey this out")
    
    def __unicode__(self):
        return "Test: " + self.specific_test + " URI: " +  self.uri

class DummyJobFile(models.Model):
    job_name = models.CharField(max_length=30, default="WO12345", unique=True, help_text="Uniquely identified jobfile name")
    work_order = models.CharField(max_length=30, default="12345", help_text="work order id") 
    notes = models.CharField(max_length=30, default="this is the default job file", help_text="Add some helpful notes in here if you create a new jobfile") 
    other_params = models.CharField(max_length=30, default="", help_text="Any other necessary params") 
    #params = models.CharField(max_length=30, default="", help_text="Any other necessary params") 

    Dummy_tests = models.ManyToManyField(DummyTest, through='LocalOverride')
    
    def __unicode__(self):
        return self.job_name

class LocalOverride(models.Model):
    job_file = models.ForeignKey(DummyJobFile)
    Dummy_test = models.ForeignKey(DummyTest)
    override_path = models.CharField(max_length=30, blank=True, help_text="The local override path, either to a specific file or a directory")
    enabled = models.BooleanField(default=True)
    
    def __unicode__(self):
        return str(self.Dummy_test)

